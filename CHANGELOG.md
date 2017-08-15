# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]


## [1.0.1] - 2017-08-15
### changed
- If there are several variants of same product template in the document (stock picking) show only one time in the notification.

## [1.0.0] - 2017-08-15
### added
- Adds new fields to model of products (product.template) that indicates if a product has accessories.
- Adds a notification in document Transfer of Stock (stock.picking) that indicates when any of the products has accessories.
