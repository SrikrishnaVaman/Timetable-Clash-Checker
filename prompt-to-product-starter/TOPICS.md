# Project topics


## How to choose

- Each pair takes **one topic**; no two pairs share a topic. Claim yours
  by writing your pair’s names in its row of the shared sheet. The first
  names in a row win.
- There are 14 topics in two categories: **City** (C1–C7) and **Campus**
  (K1–K7).
- Every topic is built to the same pattern: a few clear rules, one
  worked example, and plenty you will have to decide for yourselves.
  Deciding is part of the work: write your decisions in `spec.md`.

## What every project includes

| File | What goes in it |
|----|----|
| `spec.md` | Purpose, rules in your own words, acceptance examples, edge cases, what is out of scope |
| `tests/` | pytest tests, written before the code they test |
| your module(s) | The implementation |
| `HOW-IT-WORKS.md` | One page: how the system works and why you made the decisions you did |
| `ai-log.md` | Prompts, what you accepted or rejected and why; mark every plausible-but-wrong moment with ⚑ |
| `REVIEW.md` | Another pair’s three notes on your spec, tests and code (the class review, after sprint 4), and your response |
| `OWNERSHIP.md` | What you built, what the AI drafted, what you changed, signed by both of you (sprint 7) |

**Constraints:** Python 3 standard library plus pytest; no network
access or live data; no user interface needed (functions and tests are
enough). Use the synthetic data in the brief, or invent your own.

# City

## C1 · Coffee-shop dinner bill splitter

*City*

**The situation.** Six friends share a zi char dinner at a neighbourhood
coffee shop. Some dishes are shared by everyone, some by a few, and some
are one person’s own. The bill adds a service charge and GST, and
somebody always ends up paying a few cents too much or too little.

**What to build.**

``` python
split_bill(items, people) -> dict[str, ...]
# items: list of (dish_name, price_in_dollars, [names of people sharing it])
```

**Rules.**

1.  A dish’s price is split equally among the people sharing it.
2.  A 10% service charge is applied to the subtotal; 9% GST is then
    applied to the subtotal plus service charge.
3.  Each person pays their share of dishes, service charge and GST, in
    dollars and cents.
4.  The amounts people pay must add up **exactly** to the bill total,
    rounded to the cent.

**Example.** Chilli crab \$60.00 shared by Aisha, Ben and Chen; rice
\$3.00 for Aisha only. Subtotal \$63.00, service charge \$6.30, GST
\$6.24, total **\$75.54**. Aisha pays \$27.58, Ben \$23.98, Chen
\$23.98.

**Out of scope.** Payment methods, discounts, vouchers, a user
interface.

**Stretch goal.** Print an itemised receipt for each person.

## C2 · Bus and MRT journey fare calculator

*City*

**The situation.** A transit card records every tap in and tap out.
Riders who transfer quickly between buses and trains should be charged
for one journey, not several. You are building the fare engine that
turns a day’s taps into journeys and fares.

**What to build.**

``` python
journeys(taps) -> list[Journey]
fare(journey) -> int  # cents
# tap: (card_id, timestamp, stop_id, "in" | "out")
# distance_km(stop_a, stop_b) is supplied
```

**Rules.**

1.  A ride runs from a tap in to the next tap out on the same card.
2.  Rides belong to the same journey if the next tap in is within 45
    minutes of the previous tap out, up to 5 transfers.
3.  A journey’s fare depends on its total distance: up to 3 km \$1.00;
    up to 6 km \$1.30; up to 10 km \$1.60; over 10 km \$2.00.
4.  A ride with no tap out is charged the maximum fare (\$2.00) and ends
    the journey.

**Example.** Tap in at stop A 08:00, out at B 08:20 (4 km); in at C
08:50, out at D 09:10 (5 km). One journey of 9 km: **\$1.60**.

**Out of scope.** Concession fares, real stop data, real fare tables.

**Stretch goal.** A monthly statement per card.

## C3 · HDB-style carpark charge calculator

*City*

**The situation.** A town council’s carparks charge by the half-hour in
the day and cap the charge at night. Residents complain that the
machine’s charges are hard to predict. You are writing the calculation,
with tests clear enough to settle disputes.

**What to build.**

``` python
charge(entry: datetime, exit: datetime) -> int  # cents
```

**Rules.**

1.  Parking is charged at \$0.60 per 30 minutes or part thereof.
2.  Stays of 10 minutes or less are free.
3.  Night parking, from 22:30 to 07:00, is capped at \$5.00 per night.
4.  A stay may span several days and nights.

**Example.** Entry 09:00, exit 10:15: 75 minutes, three half-hour
blocks, **\$1.80**.

**Out of scope.** Season parking, motorcycles, real carpark data.

**Stretch goal.** Explain the charge: return a breakdown by day and
night periods.

## C4 · Community club course registration

*City*

**The situation.** A community club runs popular weekend courses
(pottery, coding for seniors, cooking). Registration opens online at 9
a.m. and the best courses fill in minutes. You are building the
registration logic, including a waitlist.

**What to build.**

``` python
register(course, person, timestamp)
withdraw(course, person, timestamp)
roster(course) -> list[str]
waitlist(course) -> list[str]
```

**Rules.**

1.  Each course has a fixed capacity.
2.  Registrations are processed in timestamp order; once a course is
    full, new registrations join its waitlist.
3.  When an enrolled person withdraws, the first person on the waitlist
    is enrolled.
4.  A person cannot hold two places (enrolled or waitlisted) on the same
    course.

**Example.** Capacity 2. Ann and Bala register, then Chen joins the
waitlist. Bala withdraws: Chen is enrolled. Roster: **Ann, Chen**;
waitlist empty.

**Out of scope.** Payment, accounts, notifications.

**Stretch goal.** Report each person’s position on every waitlist they
are on.

## C5 · Hawker stall queue-number system

*City*

**The situation.** A famous chicken rice stall issues numbered tickets
and displays the number being served. Customers wander off, miss their
call and come back. You are building the ticketing logic behind the
display.

**What to build.**

``` python
issue() -> int
call_next() -> int | None
mark_missed(number)
rejoin(number)
```

**Rules.**

1.  Tickets are numbered from 1 to 999, then start again at 1.
2.  Numbers are called in the order they were issued.
3.  A called customer who does not collect is marked missed.
4.  A missed customer may rejoin once, at the end of the queue.

**Example.** Issue 1, 2, 3. Call next: **1**. Mark 1 missed, then
rejoin 1. The remaining order is **2, 3, 1**.

**Out of scope.** Displays, printers, multiple stalls.

**Stretch goal.** Estimate waiting time per ticket from average serving
time.

## C6 · Flatmates’ utilities bill splitter

*City*

**The situation.** Flatmates in a rented HDB flat split the monthly
utilities bill. People move in and out mid-month, and the arguments are
always about days and cents. You are building a fair, checkable
calculator.

**What to build.**

``` python
split_utilities(bill_cents, period_start, period_end, stays) -> dict[str, int]
# stays: list of (name, move_in, move_out or None)
```

**Rules.**

1.  The bill covers the billing period from start to end date, both
    inclusive.
2.  Each person’s share is proportional to the number of days they
    stayed within the period.
3.  The move-in day counts as a day stayed; the move-out day does not.
4.  The shares must add up exactly to the bill.

**Example.** Period 1–30 June, bill \$90.00. Arun stays the whole period
(30 days); Bee moves in on 16 June (15 days). Arun pays **\$60.00**, Bee
**\$30.00**.

**Out of scope.** Reading meters, real tariffs, payment tracking.

**Stretch goal.** A one-line explanation of each person’s share.

## C7 · Flash-flood rain alert

*City*

**The situation.** Rain gauges across the island report every five
minutes. Heavy, short bursts of rain cause flash floods, so the agency
wants an alert as soon as rainfall in any 30-minute window crosses a
threshold. You are building the alert logic.

**What to build.**

``` python
alerts(readings, threshold_mm=20.0) -> list[Alert]
# reading: (station_id, timestamp, rainfall_mm)
```

**Rules.**

1.  Each reading is the rainfall at a station in the five minutes up to
    its timestamp.
2.  A station is in alert when the total of its readings in the last 30
    minutes (after t − 30 min, up to and including t) is at least the
    threshold.
3.  Report an alert once, at the reading that starts it; report again
    only after the station has dropped below the threshold.
4.  Readings use synthetic data; no live feeds.

**Example.** Station S1: 10:00 5 mm, 10:05 6 mm, 10:10 4 mm, 10:15 6 mm.
At 10:15 the 30-minute total is 21 mm: **alert at 10:15**.

**Out of scope.** Real data feeds, maps, notifications.

**Stretch goal.** Report when each alert ends, and its peak 30-minute
total.

# Campus

## K1 · Study room booking

*Campus*

**The situation.** Group study rooms on campus are always full in week
13. Students book them online, and double bookings cause awkward
standoffs at the door. You are writing the booking rules.

**What to build.**

``` python
book(room, student, start, end, group_size) -> Result
cancel(booking_id)
bookings_for(room, day) -> list[Booking]
```

**Rules.**

1.  Bookings are in 30-minute steps between 08:00 and 22:00.
2.  A booking may not overlap another booking of the same room. A
    booking ending at 11:00 and one starting at 11:00 do not overlap.
3.  The group size may not exceed the room’s capacity.
4.  A student may book at most 2 hours per day in total.

**Example.** Room R1: Ana books 10:00–11:00, then Ben books 11:00–12:00.
**Both succeed.** Chen’s request for 10:30–11:30 is **rejected**.

**Out of scope.** Authentication, room equipment, a calendar user
interface.

**Stretch goal.** Suggest the nearest free slot when a request is
rejected.

## K2 · Library loans and fines

*Campus*

**The situation.** The campus library lends books for two weeks, closes
on Sundays and public holidays, and charges small fines that add up.
Students dispute their fines at the counter. You are building the loan
and fine logic.

**What to build.**

``` python
due_date(borrowed_on, closures) -> date
fine(due, returned) -> int  # cents
renew(loan, today, reserved: bool) -> Loan
```

**Rules.**

1.  Loans are for 14 days. If the due date falls on a day the library is
    closed, it moves to the next open day.
2.  Fines are \$0.20 per calendar day overdue, capped at \$10.00 per
    item.
3.  A loan may be renewed at most twice, for 14 days from the renewal
    date, and not if another student has reserved the book.
4.  Closure dates (Sundays and public holidays) are supplied as a list.

**Example.** Borrowed Monday 5 October 2026: due **Monday 19 October**.
Returned Thursday 22 October: 3 days overdue, fine **\$0.60**.

**Out of scope.** Catalogue search, payments, notifications.

**Stretch goal.** A statement of all loans and fines for one student.

## K3 · Timetable clash checker

*Campus*

**The situation.** Before term starts, students juggle electives and
only discover clashes in week 3. You are building a checker that takes a
student’s chosen courses and reports every clash, week by week.

**What to build.**

``` python
clashes(sessions) -> list[Clash]
# session: (course, weekday, start, end, weeks)
# weeks: 'all', 'odd', 'even', or a list such as [1, 2, 3]
```

**Rules.**

1.  Term has teaching weeks 1 to 13; week 7 is recess with no classes.
2.  Two sessions clash if they are on the same weekday, in the same
    teaching week, and their times overlap.
3.  A session ending at 12:00 and one starting at 12:00 do not clash.
4.  Report each clash with the two courses, the weekday, the time
    overlap and the weeks affected.

**Example.** Course A: Monday 10:00–12:00, all weeks. Course B: Monday
11:00–13:00, even weeks. Clash on Monday 11:00–12:00 in weeks **2, 4, 6,
8, 10, 12**.

**Out of scope.** Real course data, room allocation, a user interface.

**Stretch goal.** Suggest an alternative session (from a supplied list)
that removes the clash.

## K4 · Makerspace 3D printer queue

*Campus*

**The situation.** The makerspace has a few 3D printers and a long queue
before project deadlines. Some students submit five jobs at once and
block everyone else. You are writing the scheduler.

**What to build.**

``` python
schedule(jobs, printers) -> list[Assignment]
# job: (job_id, student, minutes, submitted_at)
# assignment: (job_id, printer, start, end)
```

**Rules.**

1.  Jobs are considered in order of submission.
2.  Whenever a printer is free, it starts the earliest-submitted waiting
    job whose student has no job currently printing.
3.  If several printers are free at once, the lowest-numbered one is
    used.
4.  A job runs for its stated number of minutes.

**Example.** Two printers. At time 0: J1 (Sam, 60 min), J2 (Sam, 30
min), J3 (Tia, 30 min). Result: **J1 on P1 0–60, J3 on P2 0–30, J2 on P1
60–90**.

**Out of scope.** Real printer control, file handling, user accounts.

**Stretch goal.** Report each student’s waiting time.

## K5 · Group project peer-assessment calculator

*Campus*

**The situation.** Group projects end with peer assessment: each member
rates the others’ contribution, and the ratings adjust individual marks.
Students worry it is unfair; instructors worry it is gamed. You are
building the calculation.

**What to build.**

``` python
contribution_factors(ratings) -> dict[str, float]
individual_marks(team_mark, factors) -> dict[str, float]
# rating: (rater, ratee, score 1-5, submitted_at)
```

**Rules.**

1.  Each member rates every other member from 1 to 5. Self-ratings are
    ignored.
2.  A member’s factor is their average rating received divided by the
    mean of all members’ averages, rounded to 2 decimal places, and
    limited to between 0.80 and 1.10.
3.  Individual mark = team mark × factor, rounded to 1 decimal place, at
    most 100.
4.  If a rater rates the same person more than once, only the latest
    rating counts.

**Example.** Team of three, team mark 80. Asha receives 4 and 4 (average
4), Bilal 5 and 5 (5), Cai 3 and 3 (3); mean of averages 4. Factors
1.00, 1.10 (capped from 1.25), 0.80 (capped from 0.75). Marks **80.0,
88.0, 64.0**.

**Out of scope.** Collecting ratings, user accounts, dashboards.

**Stretch goal.** Flag suspicious patterns, such as a rater giving
everyone 5.

## K6 · Canteen meal-credit wallet

*Campus*

**The situation.** Hostel residents pay at the canteen with a prepaid
meal wallet. Top-ups, purchases and refunds all go through it, with a
daily spending limit to stop accidents. You are building the wallet’s
rules.

**What to build.**

``` python
top_up(wallet, amount_cents, at)
purchase(wallet, amount_cents, at) -> Result
refund(wallet, purchase_id, at) -> Result
# timestamps are ISO 8601 in UTC, for example 2026-10-27T04:30:00Z
```

**Rules.**

1.  Top-ups are at least \$5.00, and the balance may never exceed
    \$200.00.
2.  A purchase may not take the balance below zero.
3.  Total purchases per day may not exceed \$30.00. Days follow
    Singapore time (UTC+8) and reset at midnight.
4.  A purchase can be refunded only on the same day; a refund restores
    both the balance and the day’s limit.

**Example.** Top up \$20.00 at 2026-10-27T01:00Z (09:00 in Singapore).
Purchase \$4.50 at 04:30Z (12:30). Balance **\$15.50**; spent today
**\$4.50**.

**Out of scope.** Card hardware, payment gateways, user accounts.

**Stretch goal.** A daily statement in Singapore time.

## K7 · Event ticket ballot

*Campus*

**The situation.** The student council’s year-end concert has far more
applicants than seats, so tickets are allocated by ballot. Students must
be able to trust the draw. You are building a fair, reproducible ballot.

**What to build.**

``` python
run_ballot(entries, tickets, seed, ineligible) -> (winners, waitlist)
# entry: (student_id, submitted_at)
```

**Rules.**

1.  Each student may enter once; extra entries from the same student are
    ignored (the earliest counts).
2.  Students on the ineligible list are excluded.
3.  Winners are drawn at random, using the given seed so the draw can be
    reproduced.
4.  All remaining eligible entrants form a waitlist in random order.

**Example.** Entries: S1, S2, S3, S1 (again), S4; 2 tickets; no
ineligible students. Four unique entrants: **2 winners and 2 on the
waitlist**. Running again with the same seed gives the same result.

**Out of scope.** Ticket delivery, payment, user accounts.

**Stretch goal.** Publish a verification record so any student can check
the draw.
