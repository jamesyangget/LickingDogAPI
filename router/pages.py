#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from .generate import app, templates
from config import *


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def home(request: Request):
    log.info('ts,访问一次主页')
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": hometitle,
        "keywords": "API,舔狗,舔狗API,Licking Dog API,接口,FastAPI,Awesome",
        "description": description,
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get('/start.html', response_class=HTMLResponse, include_in_schema=False)
async def start(request: Request):
    log.info('ts,访问一次项目列表')
    return templates.TemplateResponse("start.html", {
        "request": request,
        "title": "项目列表",
        "keywords": "项目列表",
        "description": "项目列表",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/admin/", response_class=HTMLResponse, include_in_schema=False)
async def admin(request: Request):
    log.info('ts,访问一次后台管理')
    return templates.TemplateResponse("admin/index.html", {
        "request": request,
        "title": "后台管理 - "+hometitle,
        "keywords": "后台管理",
        "description": "后台管理",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/login/", response_class=HTMLResponse, include_in_schema=False)
async def admin(request: Request):
    log.info('ts,访问一次用户登录')
    return templates.TemplateResponse("admin/login.html", {
        "request": request,
        "title": "用户登录 - "+hometitle,
        "keywords": "用户登录",
        "description": "用户登录",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/404/", response_class=HTMLResponse, include_in_schema=False)
async def admin(request: Request):
    log.info('页面404')
    return templates.TemplateResponse("404.html", {
        "request": request,
        "title": "404 NOT FOUND",
        "keywords": "404 NOT FOUND",
        "description": "404 NOT FOUND",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get('/limit.html', response_class=HTMLResponse, include_in_schema=False)
async def limit(request: Request):
    return templates.TemplateResponse("limit.html", {
        "request": request,
    })


@app.get('/policy.html', response_class=HTMLResponse, include_in_schema=False)
async def policy(request: Request):
    log.info('ts,访问一次隐私政策页')
    return templates.TemplateResponse("policy.html", {
        "request": request,
        "title": "隐私政策",
        "keywords": "隐私政策,隐私保护,宣言,声明",
        "description": "用户隐私政策页面",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/bing/", tags=["images"])
async def bing(request: Request, type: str = None):
    import requests
    data = requests.get('https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1', headers=headers).json()
    img = {'img': 'https://cn.bing.com'+data["images"][0]["url"], 'copyright': data["images"][0]["copyright"]}
    log.info('pv,访问一次必应图片')
    return templates.TemplateResponse("items/img/bing.html", {
        "request": request,
        "title": "Bing每日一图",
        "img": img['img'] if data and type == 'img' else img,
    })


@app.get("/catvsdog.html", response_class=HTMLResponse, include_in_schema=False)
async def catvsdog(request: Request):
    log.info('ts,访问一次Cat VS Dog')
    return templates.TemplateResponse("items/ml/catvsdog.html", {
        "request": request,
        "title": "Cat VS Dog",
        "keywords": "猫狗大战,迁移学习,分类,图像,深度学习,机器学习",
        "description": "迁移学习实现猫狗识别",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/mnist.html", response_class=HTMLResponse, include_in_schema=False)
async def mnist(request: Request):
    log.info('ts,访问一次Tenserflow.js实现Mnist手写字识别')
    return templates.TemplateResponse("items/ml/mnist.html", {
        "request": request,
        "title": "Tenserflow.js实现Mnist手写字识别",
        "keywords": "手写字识别,深度学习,分类,图像,机器学习",
        "description": "迁移学习实现猫狗识别",
        "author": Copyright["author"],
        "analysis": analysis,
    })


@app.get("/ncov.html", response_class=HTMLResponse, include_in_schema=False)
async def ncov(request: Request):
    log.info('ts,访问一次2020新冠肺炎实时疫情图')
    return templates.TemplateResponse("items/ncov.html", {
        "request": request,
        "title": "2020新冠肺炎实时疫情图",
        "subtitle": "2020新冠肺炎实时疫情图",
    })
