from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from schemas import BlogCreate, BlogUpdate, BlogOut
from database import get_db, Base, engine
from models import Blog

Base.metadata.create_all(bind = engine)

api_router = APIRouter(prefix="/api/blogs")

@api_router.post("/", response_model = BlogOut)
def create_blog(blog_in: BlogCreate, db = Depends(get_db)):
    blog = Blog(
        **blog_in.model_dump()
     )
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

@api_router.get("/", response_model = list[BlogOut])
def get_blogs(db = Depends(get_db)):
    stmt = select(Blog)
    blogs = db.scalars(stmt).all()
    return blogs

@api_router.get("/id/{blog_id}", response_model = BlogOut)
def get_blog(blog_id: int, db = Depends(get_db)):
    stmt = select(Blog).where(Blog.id == blog_id)
    blog = db.scalar(stmt)

    if not blog:
        raise HTTPException(status_code = 404, detail = "Blog topilmadi")
    return blog

@api_router.get("/title/{blog_title}", response_model = BlogOut)
def get_blog(blog_title: str, db = Depends(get_db)):
    stmt = select(Blog).where(Blog.title.ilike(f"%{blog_title}%"))
    blog = db.scalar(stmt)

    if not blog:
        raise HTTPException(status_code = 404, detail = "Blog topilmadi")
    return blog

@api_router.put("/id/{blog_id}", response_model = BlogOut)
def update_blog(blog_id: int, blog_in: BlogUpdate, db = Depends(get_db)):
    stmt = select(Blog).where(Blog.id == blog_id)
    blog = db.scalar(stmt)

    if not blog:
        raise HTTPException(status_code = 404, detail = "Blog topilmadi")

    for key, value in blog_in.model_dump(exclude_unset=True).items():
        setattr(blog, key, value)

    db.commit()
    db.refresh(blog)
    return blog

@api_router.delete("/{blog_id}")
def delete_blog(blog_id: int, db = Depends(get_db)):
    stmt = select(Blog).where(Blog.id == blog_id)
    blog = db.scalar(stmt)

    if not blog:
        raise HTTPException(status_code = 404, detail = "Blog topilmadi")

    db.delete(blog)
    db.commit()
    return HTTPException(status_code = 200, detail = "Blog o'chirildi")



