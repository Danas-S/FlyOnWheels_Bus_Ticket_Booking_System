# Week 10 Video Talking Points (Full Code Walkthrough)

## 1. Opening (20-30 seconds)
- This project is a menu-driven transport booking system.
- It has two parts:
   - Part 1: class model and persistence setup.
   - Part 2: runnable program with admin/customer flows and tests.
- Mention that `test_main.py` passes and you will show code evidence.

## 2. Class Diagram and Class Files (1-2 minutes)
- Show the class diagram image in `week10`.
- Explain each class file maps to one table concept:
   - `user.py` -> `User`
   - `service.py` -> `Service`
   - `run.py` -> `Run`
   - `bus_model.py` -> `BusModel`
   - `bus.py` -> `Bus`
   - `ticket.py` -> `Ticket`
- Explain relationships in plain language:
   - One `Service` has many `Run` rows.
   - One `Service` has two `Bus` schedule assignments.
   - `Bus` references `BusModel` for seat capacity.
   - `User` owns `Ticket` rows.
   - `Ticket` links to a specific `Run`.

## 3. Database Creation and Seed Logic (2 minutes)
- Open `create_database.py`.
- Explain constants and helpers:
   - `DB_PATH` centralizes DB filename.
   - `hash_password()` secures stored passwords.
- Explain `create_database()` end-to-end:
   - Rebuilds schema with singular table names expected by tests.
   - Creates `user`, `service`, `bus_model`, `run`, `bus`, `ticket`.
   - Seeds Bob admin, 3 services, 2 bus models.
   - Generates 7 days of runs for each service.
   - Adds 2 buses per service (A weekend, B workday).
   - Adds initial ticket row for Bob.
- Mention this function is used by both tests and `main.py` startup.

## 4. Main Program Architecture (2-3 minutes)
- Open `main.py`.
- Walk through structure top to bottom:
   - Data/auth helpers:
      - `hash_password`, `open_connection`, `authenticate_user`, `create_account`.
   - Admin operations:
      - `list_services`, `create_service`.
   - Customer operations:
      - `list_future_runs`, `buy_tickets`, `list_user_tickets`.
   - Output helpers:
      - `print_services`, `print_future_runs`, `print_user_tickets`.
   - Menu controllers:
      - `admin_menu`, `customer_menu`, `home_menu`, `main`.
- Explain role-based routing:
   - Home login checks `admin` flag.
   - Admin users go to admin menu.
   - Ordinary users go to customer menu.

## 5. Required Menus and User Journey (1-2 minutes)
- Home menu options:
   - Log in, Create account, Exit.
- Admin menu options:
   - View services, Create service, Log out.
- Customer menu options:
   - View future runs, Buy tickets, View bought tickets, Log out.
- Describe demo journey used by tests:
   - Bob logs in and adds Dundalk service.
   - Betty account is created and logs in.
   - Betty buys tickets, cancels once, and attempts overbooking.

## 6. Two Problems Fixed (required by brief)
### Fix 1: Schema mismatch with tests
- Problem: initial code used plural table names from Part 1.
- Fix: `create_database()` now builds singular schema expected by `test_main.py`.
- Result: application queries and test assertions operate on same structure.

### Fix 2: Booking flow/test-sequence mismatch
- Problem: confirmation prompt appeared even when seats were insufficient, causing input drift.
- Fix: `customer_menu()` validates selection and availability before confirmation prompt.
- Related fix: run selection treated as displayed list index, not raw DB id.
- Result: scenario input sequence stays aligned and test flow is stable.

## 7. Two Quality Areas Good From The Start (required by brief)
### Quality 1: Separation of concerns
- Data operations are isolated from menu control flow.
- Print helpers avoid duplicating output logic.

### Quality 2: Input safety and transaction handling
- Numeric parsing and selection bounds are validated.
- Account creation handles duplicates via integrity error checks.
- Connections are closed safely using `try/finally`.

## 8. Testing Evidence (30-45 seconds)
- Run from `week10` directory:
   - `python -m unittest test_main.py`
- Show `OK` result and mention both scenario/output and DB-state tests pass.
- Optionally show `test_database.py` output for table inspection.

## 9. Files to Show on Screen (quick checklist)
- `create_database.py`
- `main.py`
- `test_main.py`
- `test_database.py`
- `user.py`, `service.py`, `run.py`, `bus_model.py`, `bus.py`, `ticket.py`
- class diagram image in `week10`
- `url_link.txt`

## 10. Closing (10-15 seconds)
- Summarize that all required menus, persistence, tests, and quality discussion points are complete.
- Confirm branch workflow was used and work is ready to merge to `main`.
