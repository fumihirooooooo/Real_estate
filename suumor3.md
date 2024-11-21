```mermaid
classDiagram
    direction TB

    class Main {
        - int max_page
        - str url
        - Time time
        - GetInfoSuumo getinfosuumo
        - ToExcel toexcel
    }

    class Time {
        + measure_time()
    }
    
    class GetInfoSuumo{
        - str url
        + __init__(url: str)
        + load_page(url: str): BeautifulSoup 
        + scrape() List[Dict[str, str]]
    }

    class GetInfo{
        + load_page(url: str): BeautifulSoup 
        + scrape() List[Dict[str, str]]
    }

    class ToExcel{
        + ToExcel()
    }

GetInfo <|-- GetInfoSuumo

Main --> GetInfoSuumo
Main --> Time
Main --> ToExcel
