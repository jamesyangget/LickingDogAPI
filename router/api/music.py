from starlette.status import HTTP_404_NOT_FOUND
from starlette.responses import JSONResponse
from items.music import CloudMusic, QQ, music_type
from items import Charts, Music
from fastapi import APIRouter
from config import log, Copyright
import time
router = APIRouter()


@router.get("/cloudmusic/")
async def cloud_music(type: Music.Type, id: int):
    log.info('pv,请求一次网易云音乐api')
    return {
        "code": 200,
        "copyright": Copyright,
        "data": music_type(CloudMusic, type, id),
        "time": time.ctime(),
    }


@router.get("/qq/")
async def qq_music(type: Music.Type, id: int):
    log.info('pv,请求一次QQ音乐api')

    return {
        "code": 200,
        "copyright": Copyright,
        "data": music_type(QQ, type, id),
        "time": time.ctime(),
    }


@router.get("/billboard/{chart}")
async def billboard(chart: Charts):
    from items.billboard import get_content
    log.info('pv,请求一次公告牌数据')
    if chart in (Charts.hot100, Charts.billboard200,
                 Charts.artist100, Charts.social50):
        return {
            "code": 200,
            "copyright": Copyright,
            "data": get_content(chart),
            "time": time.ctime(),
        }
    else:
        return JSONResponse(status_code=HTTP_404_NOT_FOUND,
                            content={'msg': f'{chart} is not found'})