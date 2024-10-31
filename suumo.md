```mermaid
classDiagram
    class Scrape {
        - String url
        - int max_page
        + loadPage(url: String): Soup
        + measure_time()
        + scrape()
    }

    class data_home {
        + String category
        + String name
        + String adress
        + String near_station
        + String age_and_floors
    }

    class data_room{
        + String price
        + String price_andadministration
        + String price_deposit
        + String price_gratuity
        + String madori
        + String menseki   
    }


    Scrape<|--data_home 
    Scrape<|--data_room




