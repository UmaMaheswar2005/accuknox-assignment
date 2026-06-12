# AccuKnox Django Trainee Assignment

A Django project demonstrating default Django signal behaviors and Python class iteration.

## Project Structure
The project is divided into two Django apps:
1. `signals_demo`: Contains the models, signals, and tests proving synchronous, thread-sharing, and transaction-sharing behaviors.
2. `custom_classes`: Contains the custom iterable `Rectangle` class.

---

## Part 1 — Django Signals

### Q1: Are Django signals synchronous or asynchronous?
**Answer: Synchronous.**
By default, Django signals execute synchronously. The caller block must wait for the signal handler to finish its execution before it can continue. 

**Proof:** In `signals_demo/tests.py`, the `test_q1_signals_are_synchronous` test triggers a signal that sleeps for 2 seconds. The test asserts that the total execution time of the `.create()` call takes $\ge$ 2 seconds, proving the caller was blocked.

### Q2: Do Django signals run in the same thread as the caller?
**Answer: Yes.**
By default, standard Django signals run in the exact same thread as the caller. 

**Proof:** In `signals_demo/tests.py`, the `test_q2_signals_share_caller_thread` test captures the thread ID of the caller, and compares it to the thread ID captured inside the signal handler. They match perfectly.

### Q3: Do Django signals run in the same DB transaction as the caller?
**Answer: Yes (by default).**
Signal handlers share the caller's open database transaction. If an error occurs inside the signal, the entire transaction (including the caller's database operations) is rolled back.

**Proof:** In `signals_demo/tests.py`, the `test_q3_signals_share_caller_transaction` test wraps a model creation in `transaction.atomic()`. The signal intentionally throws an exception. The test verifies that the model was never saved to the database, proving the rollback occurred across both scopes.

---

## Part 2 — Custom Classes

The implementation for the custom iterable class is located at `custom_classes/rectangle.py`. It utilizes the `__iter__` dunder method with `yield` statements to return the required dictionary formats.

---

## Setup & Running Tests

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd <your-repo-folder>

# 2. Install dependencies
pip install django

# 3. Apply migrations
python manage.py migrate

# 4. Run the tests to prove all behaviors
python manage.py test
```