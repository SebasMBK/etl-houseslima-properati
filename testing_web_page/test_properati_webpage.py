import requests
import pytest

@pytest.fixture(scope="function")
def data_scraper():
    url = "https://www.properati.com.pe/_next/data/dEkpljIH4oO661olRxF4i/s/lima/venta/tipo%3Adepartamento%2Ccasa.json"
    querystring = {"page":"1","search_params":["lima","venta","tipo:departamento,casa"]}
    payload = ""
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
            "Accept": "*/*",
            "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.properati.com.pe/s/lima/venta/tipo:departamento,casa",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "Connection": "keep-alive",
            "Cookie": "page_view_id=466e10e1; _gcl_au=1.1.1429795133.1670166437; __utmz=1.1.1.1.source=direct; _ga_XBCJTXSM9R=GS1.1.1670169881.2.1.1670170352.0.0.0; _ga=GA1.3.1459168715.1670166438; _ga_T5QNJM00PN=GS1.1.1670169881.2.1.1670170352.0.0.0; _ga_CK4G1405CS=GS1.1.1670169881.2.1.1670170352.0.0.0; access_token=eyJhbGciOiJSUzI1NiIsImtpZCI6Ijk1MWMwOGM1MTZhZTM1MmI4OWU0ZDJlMGUxNDA5NmY3MzQ5NDJhODciLCJ0eXAiOiJKV1QifQ.eyJwcm92aWRlcl9pZCI6ImFub255bW91cyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9wcm9wZXJhdGktYXBpLWFjdGl2aXR5LXByZCIsImF1ZCI6InByb3BlcmF0aS1hcGktYWN0aXZpdHktcHJkIiwiYXV0aF90aW1lIjoxNjcwMTY2NDM4LCJ1c2VyX2lkIjoieHZwdGl3RWljUVduYW03Z016d29ReE5JNUo2MyIsInN1YiI6Inh2cHRpd0VpY1FXbmFtN2dNendvUXhOSTVKNjMiLCJpYXQiOjE2NzAxNjY0MzgsImV4cCI6MTY3MDE3MDAzOCwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6e30sInNpZ25faW5fcHJvdmlkZXIiOiJhbm9ueW1vdXMifX0.NQaallbH4MKFV4V3LqZRPrNWnl377GGFbZrVWlNqat5UQOqEv4GY4-LGmn1M4M8MW7J3nevFHbYmDyU687MZGYrwyCWhyAgVSV9X5waeW81RbEtbur1KaWtFBtyDkskGWYDHEFufKA7FhbWpTPjukVqFYyGKZPatQCku1tOn8V8HBH_64GxNJJG0kzrrdMBAfSTnqDRU_oU1KbkXUPK2YSG6jnwOtdba7YxDXZvA0MOyhKcXXUqIfWOSw-wCbe9LkYQDPU9Kp1lSMb0eX_QW2Yjz4teJ3XcFsfrYFvXOx19yY35ga68PWabvLRZM5PFk6xH8vjHshJsRMY1twJCD3A; firebase_user_id=xvptiwEicQWnam7gMzwoQxNI5J63; _gid=GA1.3.1654845518.1670166440; _fbp=fb.2.1670166441919.694238004; _hjSessionUser_1242563=eyJpZCI6Ijc3NTM0MjcwLTc5M2QtNWZmYS05ODhkLWFhNzc0MmRiNDVlMyIsImNyZWF0ZWQiOjE2NzAxNjY0NDIwNzMsImV4aXN0aW5nIjp0cnVlfQ==; _hjIncludedInSessionSample=0; WZRK_S_4W5-ZWK-KW6Z=%7B%22p%22%3A3%7D; _hjSession_1242563=eyJpZCI6ImMyMTI4MGM5LTA4NGQtNDAxMy1iYTc3LTNiNzlkZmRkYWUxNyIsImNyZWF0ZWQiOjE2NzAxNjk4ODI4ODMsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInPageviewSample=1; _hjAbsoluteSessionInProgress=0"
        }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    
    return response

# Make sure we are getting a proper response
def test_code_status(data_scraper):
    assert data_scraper.status_code == 200

# Make sure we get a limit of 30 items per page
def test_limit_of_items_per_page(data_scraper):
    assert len(data_scraper.json()['pageProps']['results']['data']) <= 30

