# OpenWebUI API Schema Exports

*Last updated: March 23, 2025*

![OpenWebUI API Documentation Example](screenshots/1.png)

## Overview

This repository provides an unofficial export of the OpenWebUI OpenAPI definitions, retrieved from the Swagger documentation. These exports are organized into structured JSON and Markdown files for easier reference and integration.

## Accessing OpenWebUI API Documentation

To access the API documentation on any OpenWebUI instance:

1. Enable the development environment by setting:
   ```
   ENV=dev
   ```

2. Navigate to `yourinstance.com/docs` to view the interactive Swagger documentation.

## Repository Contents

This repository contains:

- Raw schema exports from the OpenWebUI API documentation
- Categorized endpoint documentation organized by API section
- Both JSON and Markdown formats for different use cases

## Using the Extract Script

The `scripts/extract.py` script can be used to generate fresh exports from an OpenAPI definition file:

```bash
# Place your OpenAPI JSON file as input.json in the root directory
# Then run:
python scripts/extract.py
```

The script will:
- Extract all paths with the prefix `/api/v1/`
- Generate separate JSON files for each endpoint
- Create Markdown documentation with details for each endpoint
- Organize outputs by API category (e.g., knowledge, chat, etc.)

## Purpose

These exports are useful for:
- Understanding the OpenWebUI API structure
- Building integrations with OpenWebUI
- Documenting specific endpoints for reference
- Tracking API changes between versions