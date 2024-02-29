# Sreality scrapy

## Description

Project for scraping sreality using simple docker-compose up command

## Installation

- Run `docker-compose up` in the folder, and then open http://localhost:8080

## Usage

- After running docker compose the page will startup on [localhost:8080](http://localhost:8080)
- Alternatively you can use vs code devcontainers with debug to test scripts manually
    - Here you need to first run `scrapy crawl sreality` in folder `sreality_scrapy`
    - And then you can debug app.py

## Assignment definition
```Use scrapy framework to scrape the first 500 items (title, image url) from sreality.cz (flats, sell) and save it in the Postgresql database. Implement a simple HTTP server in python and show these 500 items on a simple page (title and image) and put everything to single docker compose command so that I can just run "docker-compose up" in the Github repository and see the scraped ads on http://127.0.0.1:8080 page.```