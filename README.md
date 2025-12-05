# Tikiti Yangu Backend

Tikiti Yangu is a backend system for managing users, events, tickets, and ticket status tracking.  
This backend is built using **Python**, **SQLAlchemy**, and **SQLite** (or any SQL database) and provides a CLI and database layer for managing data efficiently.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [CLI Usage](#cli-usage)
- [API / Models](#api--models)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Manage Users, Drivers, Locations, Parcels, Routes, and Parcel Status Updates
- CLI commands for creating, listing, assigning, and tracking parcels
- Database management with SQLAlchemy ORM
- Optional integration with Alembic for migrations
- Supports SQLite (default) and other SQL databases like PostgreSQL

---

## Tech Stack

- Python 3.11+
- SQLAlchemy ORM
- SQLite (default, can be replaced with PostgreSQL/MySQL)
- Click (for CLI commands)
- Alembic (optional for migrations)

---

## Project Structure

