"""Manage school bus riders, route rosters, fees, and dispatch alerts."""

import sqlite3

CONNECTION = sqlite3.connect(":memory:")

CONNECTION.execute(
    """
    CREATE TABLE riders (
        id INTEGER PRIMARY KEY,
        student TEXT,
        route TEXT,
        stop TEXT,
        fee INTEGER
    )
    """
)


def enroll_rider(student, route, stop, fee):
    """Register a student for a bus route."""
    CONNECTION.execute(
        """
        INSERT INTO riders (student, route, stop, fee)
        VALUES (?, ?, ?, ?)
        """,
        (student, route, stop, fee),
    )
    CONNECTION.commit()


def route_roster(route):
    """Return the student names registered for a route."""
    cursor = CONNECTION.execute(
        "SELECT student FROM riders WHERE route = ?",
        (route,),
    )
    return [row[0] for row in cursor]


def export_roster(path, route):
    """Write a route's student roster to a text file."""
    with open(path, "w", encoding="utf-8") as output:
        for name in route_roster(route):
            output.write(f"{name}\n")


def dispatch_alert(route):
    """Display a bus dispatch alert."""
    print(f"dispatching bus {route}")


def fee_collected(route):
    """Return the total fees collected for a route."""
    result = CONNECTION.execute(
        "SELECT SUM(fee) FROM riders WHERE route = ?",
        (route,),
    ).fetchone()
    total = result[0]
    return total if total is not None else 0


def main():
    """Run the school bus transport demonstration."""
    enroll_rider("Tara", "R1", "Lake Road", 1800)
    enroll_rider("Kabir", "R1", "Mill Street", 1800)
    enroll_rider("Zoya", "R2", "Fort Gate", 2100)

    if fee_collected("R1") != 3600:
        raise RuntimeError("Fee total validation failed for route R1")

    export_roster("route_r1.txt", "R1")
    dispatch_alert("R1")
    print(route_roster("R2"))


if __name__ == "__main__":
    main()
