from datetime import datetime, timedelta
from pathlib import Path


from fastapi import Cookie, Depends, Query, Request
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.routing import APIRouter

from ai_art_landing.helpers import template_renderer
from ai_art_landing.settings import settings


generic_router = APIRouter(
    tags=["Core NON-API Website Routes"], include_in_schema=False
)


@generic_router.get("/favicon.ico", response_class=FileResponse)
async def favicon():
    return FileResponse(Path("ai_art_landing", "static", "favicon.ico"))


@generic_router.get("/", response_class=HTMLResponse)
async def home(request: Request, lightning: str = "ok too"):
    # Hardcoded monthly data that would have come from gen_monthly_report
    monthly_data = [
    {
        "date": "2018-03-01",
        "cash_asset": 10000.0,
        "cash_asset_pct": 0.0
    },
    {
        "date": "2018-03-31",
        "cash_asset": 12313.76861987,
        "cash_asset_pct": 23.137686198699996
    },
    {
        "date": "2018-04-30",
        "cash_asset": 13200.54922945,
        "cash_asset_pct": 32.0054922945
    },
    {
        "date": "2018-05-31",
        "cash_asset": 14361.77431218,
        "cash_asset_pct": 43.6177431218
    },
    {
        "date": "2018-06-30",
        "cash_asset": 15255.31034056,
        "cash_asset_pct": 52.5531034056
    },
    {
        "date": "2018-07-31",
        "cash_asset": 15180.59279585,
        "cash_asset_pct": 51.8059279585
    },
    {
        "date": "2018-08-31",
        "cash_asset": 14750.58270651,
        "cash_asset_pct": 47.50582706510001
    },
    {
        "date": "2018-09-30",
        "cash_asset": 15546.72070061,
        "cash_asset_pct": 55.4672070061
    },
    {
        "date": "2018-10-31",
        "cash_asset": 15462.7530862,
        "cash_asset_pct": 54.62753086200001
    },
    {
        "date": "2018-11-30",
        "cash_asset": 16512.0546807,
        "cash_asset_pct": 65.120546807
    },
    {
        "date": "2018-12-31",
        "cash_asset": 20096.17056481,
        "cash_asset_pct": 100.96170564809998
    },
    {
        "date": "2019-01-31",
        "cash_asset": 19017.91096454,
        "cash_asset_pct": 90.17910964539999
    },
    {
        "date": "2019-02-28",
        "cash_asset": 20112.34344729,
        "cash_asset_pct": 101.1234344729
    },
    {
        "date": "2019-03-31",
        "cash_asset": 20089.0703739,
        "cash_asset_pct": 100.89070373899997
    },
    {
        "date": "2019-04-30",
        "cash_asset": 21160.3147769,
        "cash_asset_pct": 111.60314776899997
    },
    {
        "date": "2019-05-31",
        "cash_asset": 21791.34170001,
        "cash_asset_pct": 117.91341700010001
    },
    {
        "date": "2019-06-30",
        "cash_asset": 26154.25923967,
        "cash_asset_pct": 161.5425923967
    },
    {
        "date": "2019-07-31",
        "cash_asset": 27184.36129864,
        "cash_asset_pct": 171.84361298640002
    },
    {
        "date": "2019-08-31",
        "cash_asset": 27013.83769284,
        "cash_asset_pct": 170.1383769284
    },
    {
        "date": "2019-09-30",
        "cash_asset": 26783.67686296,
        "cash_asset_pct": 167.83676862960002
    },
    {
        "date": "2019-10-31",
        "cash_asset": 27871.38447427,
        "cash_asset_pct": 178.7138447427
    },
    {
        "date": "2019-11-30",
        "cash_asset": 26265.2530021,
        "cash_asset_pct": 162.65253002099996
    },
    {
        "date": "2019-12-31",
        "cash_asset": 26653.06751749,
        "cash_asset_pct": 166.53067517489998
    },
    {
        "date": "2020-01-31",
        "cash_asset": 25805.42368482,
        "cash_asset_pct": 158.05423684820002
    },
    {
        "date": "2020-02-29",
        "cash_asset": 26160.702407,
        "cash_asset_pct": 161.60702407
    },
    {
        "date": "2020-03-31",
        "cash_asset": 35350.15182554,
        "cash_asset_pct": 253.5015182554
    },
    {
        "date": "2020-04-30",
        "cash_asset": 37757.09225165,
        "cash_asset_pct": 277.5709225165
    },
    {
        "date": "2020-05-31",
        "cash_asset": 37520.1307872,
        "cash_asset_pct": 275.20130787200003
    },
    {
        "date": "2020-06-30",
        "cash_asset": 37515.20879417,
        "cash_asset_pct": 275.1520879417
    },
    {
        "date": "2020-07-31",
        "cash_asset": 36837.3117127,
        "cash_asset_pct": 268.373117127
    },
    {
        "date": "2020-08-31",
        "cash_asset": 36582.30802835,
        "cash_asset_pct": 265.8230802835
    },
    {
        "date": "2020-09-30",
        "cash_asset": 35858.60551542,
        "cash_asset_pct": 258.5860551542
    },
    {
        "date": "2020-10-31",
        "cash_asset": 35570.77977333,
        "cash_asset_pct": 255.70779773330003
    },
    {
        "date": "2020-11-30",
        "cash_asset": 38697.01971347,
        "cash_asset_pct": 286.97019713469996
    },
    {
        "date": "2020-12-31",
        "cash_asset": 44314.02568648,
        "cash_asset_pct": 343.1402568648
    },
    {
        "date": "2021-01-31",
        "cash_asset": 55997.19992335,
        "cash_asset_pct": 459.9719992335
    },
    {
        "date": "2021-02-28",
        "cash_asset": 59529.74510817,
        "cash_asset_pct": 495.29745108169993
    },
    {
        "date": "2021-03-31",
        "cash_asset": 54070.51088367,
        "cash_asset_pct": 440.7051088367
    },
    {
        "date": "2021-04-30",
        "cash_asset": 55323.50806071,
        "cash_asset_pct": 453.23508060710003
    },
    {
        "date": "2021-05-31",
        "cash_asset": 60133.00790968,
        "cash_asset_pct": 501.3300790968
    },
    {
        "date": "2021-06-30",
        "cash_asset": 68163.45240722,
        "cash_asset_pct": 581.6345240722
    },
    {
        "date": "2021-07-31",
        "cash_asset": 67438.5655705,
        "cash_asset_pct": 574.385655705
    },
    {
        "date": "2021-08-31",
        "cash_asset": 63509.98605973,
        "cash_asset_pct": 535.0998605973
    },
    {
        "date": "2021-09-30",
        "cash_asset": 56236.35794157,
        "cash_asset_pct": 462.3635794157
    },
    {
        "date": "2021-10-31",
        "cash_asset": 62373.72279957,
        "cash_asset_pct": 523.7372279957001
    },
    {
        "date": "2021-11-30",
        "cash_asset": 59765.35010055,
        "cash_asset_pct": 497.65350100549995
    },
    {
        "date": "2021-12-31",
        "cash_asset": 60401.98884095,
        "cash_asset_pct": 504.0198884095
    },
    {
        "date": "2022-01-31",
        "cash_asset": 44916.72050648,
        "cash_asset_pct": 349.1672050648
    },
    {
        "date": "2022-02-28",
        "cash_asset": 50930.90349385,
        "cash_asset_pct": 409.3090349385
    },
    {
        "date": "2022-03-31",
        "cash_asset": 54504.00578337,
        "cash_asset_pct": 445.04005783369996
    },
    {
        "date": "2022-04-30",
        "cash_asset": 53444.97094939,
        "cash_asset_pct": 434.4497094939
    },
    {
        "date": "2022-05-31",
        "cash_asset": 52885.34466678,
        "cash_asset_pct": 428.85344666780003
    },
    {
        "date": "2022-06-30",
        "cash_asset": 62626.63778836,
        "cash_asset_pct": 526.2663778836
    },
    {
        "date": "2022-07-31",
        "cash_asset": 53163.57587073,
        "cash_asset_pct": 431.6357587073
    },
    {
        "date": "2022-08-31",
        "cash_asset": 53163.62029403,
        "cash_asset_pct": 431.6362029403
    },
    {
        "date": "2022-09-30",
        "cash_asset": 55580.94217592,
        "cash_asset_pct": 455.8094217592
    },
    {
        "date": "2022-10-31",
        "cash_asset": 57841.54331198,
        "cash_asset_pct": 478.41543311979996
    },
    {
        "date": "2022-11-30",
        "cash_asset": 59619.80107936,
        "cash_asset_pct": 496.1980107935999
    },
    {
        "date": "2022-12-31",
        "cash_asset": 57468.91015266,
        "cash_asset_pct": 474.6891015266
    },
    {
        "date": "2023-01-31",
        "cash_asset": 58210.54354999,
        "cash_asset_pct": 482.1054354999
    },
    {
        "date": "2023-02-28",
        "cash_asset": 61198.03088322,
        "cash_asset_pct": 511.9803088322
    },
    {
        "date": "2023-03-31",
        "cash_asset": 60857.93711635,
        "cash_asset_pct": 508.57937116350007
    },
    {
        "date": "2023-04-30",
        "cash_asset": 61814.36728728,
        "cash_asset_pct": 518.1436728728
    },
    {
        "date": "2023-05-31",
        "cash_asset": 60125.11329288,
        "cash_asset_pct": 501.2511329288
    },
    {
        "date": "2023-06-30",
        "cash_asset": 59567.40202393,
        "cash_asset_pct": 495.67402023930003
    },
    {
        "date": "2023-07-31",
        "cash_asset": 59258.57058565,
        "cash_asset_pct": 492.58570585649994
    },
    {
        "date": "2023-08-31",
        "cash_asset": 58651.02901547,
        "cash_asset_pct": 486.5102901547
    },
    {
        "date": "2023-09-30",
        "cash_asset": 57047.27917023,
        "cash_asset_pct": 470.4727917023
    },
    {
        "date": "2023-10-31",
        "cash_asset": 58779.589836,
        "cash_asset_pct": 487.79589836
    },
    {
        "date": "2023-11-30",
        "cash_asset": 61556.49289191,
        "cash_asset_pct": 515.5649289191
    },
    {
        "date": "2023-12-31",
        "cash_asset": 62330.92039331,
        "cash_asset_pct": 523.3092039331
    },
    {
        "date": "2024-01-31",
        "cash_asset": 68962.98140296,
        "cash_asset_pct": 589.6298140296
    },
    {
        "date": "2024-02-29",
        "cash_asset": 70333.36807015,
        "cash_asset_pct": 603.3336807015
    },
    {
        "date": "2024-03-31",
        "cash_asset": 82872.13922149,
        "cash_asset_pct": 728.7213922148999
    },
    {
        "date": "2024-04-30",
        "cash_asset": 83994.39363497,
        "cash_asset_pct": 739.9439363496999
    },
    {
        "date": "2024-05-31",
        "cash_asset": 91013.61958169,
        "cash_asset_pct": 810.1361958169001
    },
    {
        "date": "2024-06-30",
        "cash_asset": 92455.62313398,
        "cash_asset_pct": 824.5562313398001
    },
    {
        "date": "2024-07-31",
        "cash_asset": 92860.77166932,
        "cash_asset_pct": 828.6077166932001
    },
    {
        "date": "2024-08-31",
        "cash_asset": 93542.1514803,
        "cash_asset_pct": 835.421514803
    },
    {
        "date": "2024-09-30",
        "cash_asset": 94063.49969024,
        "cash_asset_pct": 840.6349969024
    },
    {
        "date": "2024-10-31",
        "cash_asset": 92723.3617675,
        "cash_asset_pct": 827.233617675
    },
    {
        "date": "2024-11-30",
        "cash_asset": 90094.20019852,
        "cash_asset_pct": 800.9420019851999
    },
    {
        "date": "2024-12-12",
        "cash_asset": 93207.38819923,
        "cash_asset_pct": 832.0738819922999
    }
    ]

    # Extract the dates and percentage values
    chart_data = {
        "dataset1": [entry['cash_asset_pct'] for entry in monthly_data]
        #, "dataset2": [entry['price_pct'] for entry in monthly_data]
    }

    content = {
        "lnurl": lightning,
        "chart_data": chart_data
    }

    response = template_renderer().TemplateResponse(
        request, "core/index.html", content
    )

    # Add cache headers for 3 days
    response.headers["Cache-Control"] = "public, max-age=259200"
    response.headers["Expires"] = (datetime.now() + timedelta(days=3)).strftime("%a, %d %b %Y %H:%M:%S GMT")

    return response


@generic_router.get("/terms-services.html", response_class=HTMLResponse)
async def home(request: Request, lightning: str = "ok"):
    content = {"lnurl": lightning}
    return template_renderer().TemplateResponse(
        request, "core/terms-services.html", content
    )


@generic_router.get("/privacy-policy.html", response_class=HTMLResponse)
async def home(request: Request, lightning: str = "ok"):
    content = {"lnurl": lightning}
    return template_renderer().TemplateResponse(
        request, "core/privacy-policy.html", content
    )


@generic_router.get("/about-us.html", response_class=HTMLResponse)
async def home(request: Request, lightning: str = "ok"):
    content = {"lnurl": lightning}
    return template_renderer().TemplateResponse(
        request, "core/about-us.html", content
    )
