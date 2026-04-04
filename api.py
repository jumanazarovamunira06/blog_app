from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas import BlogCreate, BlogUpdate, BlogOut, UserCreate, UserOut
from database import get_db, Base, engine
from models import Blog, User

Base.metadata.create_all(bind=engine)

api_router = APIRouter(prefix="/api/blogs")

@api_router.post("/users", response_model=UserOut)
def create_user(user_in: UserCreate, db: Session = Depends(get_db)):
    user = User(**user_in.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@api_router.get("/users", response_model=list[UserOut])
def get_users( db: Session = Depends(get_db)):
    stmt = select(User)
    users = db.scalars(stmt).all()

    
    return users




@api_router.post("/", response_model=BlogOut)
def create_blog(blog_in:BlogCreate ,db:Session=Depends(get_db)):
    user_stmt=select(User).where(User.id==blog_in.user_id)
    user=db.scalar(user_stmt)
    if not user :
        raise HTTPException(status_code=400,detail=f"{blog_in.user_id} id li user mavjud emas")
    blog=Blog(**blog_in.model_dump())
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog




@api_router.get("/",response_model=list[BlogOut])
def get_blogs(db :Session=Depends(get_db)):
    stmt =select(Blog)
    blogs=db.scalars(stmt).all()
    return blogs


@api_router.get("/id/{blog_id}", response_model=list[BlogOut])
def get_blog_by_id(blog_id: int, db: Session = Depends(get_db)):
    stmt = select(Blog).where(Blog.id == blog_id)
    blog = db.scalar(stmt)

    if not blog:
        raise HTTPException(status_code=404, detail="Blog topilmadi")
    return blog



@api_router.get("/title/{blog_title}", response_model=BlogOut)
def get_blog_by_title(blog_title: str, db: Session = Depends(get_db)):
    stmt = select(Blog).where(Blog.title.ilike(f"%{blog_title}%"))
    blog = db.scalar(stmt)

    if not blog:
        raise HTTPException(status_code=404, detail="Blog topilmadi")
    return blog






@api_router.put("/id/{blog_id}", response_model=BlogOut)
def update_blog(blog_id: int, blog_in: BlogUpdate, db: Session = Depends(get_db)):
    stmt = select(Blog).where(Blog.id == blog_id)
    blog = db.scalar(stmt)

    if not blog:
        raise HTTPException(status_code=404, detail="Blog topilmadi")

    for key, value in blog_in.model_dump(exclude_unset=True).items():
        setattr(blog, key, value)

    db.commit()
    db.refresh(blog)
    return blog

@api_router.delete("/id/{blog_id}") # '/id/' qo'shildi
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    stmt = select(Blog).where(Blog.id == blog_id)
    blog = db.scalar(stmt)

    if not blog:
        raise HTTPException(status_code=404, detail="Blog topilmadi")

    db.delete(blog)
    db.commit()
    return {"detail": "Blog o'chirildi"}


