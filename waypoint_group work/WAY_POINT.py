"""Scenario: You are developing a navigation system that needs to track routes as a sequence of waypoints. Each waypoint has a location and a description. The system needs to support operations to add and remove waypoints, as well as to move

through them in both directions (i.e., to the next or previous waypoint).

Task:

1. Waypoint Node: Define a Waypoint class that can represent each waypoint with attributes for the location, description, and links to any next or previous waypoints.

2. Route Tracker:

• Implement a Route class using a singly linked list. This should allow waypoints to be traversed in a forward direction only.

• Extend the Route class to a BidirectionalRoute class using a doubly linked list, allowing traversal in both forward and backward directions.

3. Core Functionalities:

⚫For both classes, implement methods to add_waypoint(location, description) at the end of the route.

• Implement methods to insert waypoint_after(target, location, description) where target is an existing waypoint after which you want to insert the new one.

• Implement methods to remove_waypoint(location) that will find a

waypoint by location and remove it from the route. Implement traversal methods next waypoint) and previous waypoint() for the Bidirectional Route.

4. Demonstration:

Create a test scenario where you construct a route with at least 5 waypoints.

•Demonstrate adding, inserting, and removing waypoints.

⚫Show how you can traverse the waypoints in a single direction using the Route class.

• Show bidirectional traversal using the BidirectionalRoute class.
Write a code for this in python using linked lists"""


# Define a class representing a Waypoint
class Waypoint:
    def __init__(self, location, description):
        self.location = location          # Initialize the location attribute
        self.description = description    # Initialize the description attribute
        self.next = None                  # Initialize the next attribute to None
        self.prev = None                  # Initialize the prev attribute to None

# Define a class representing a Route
class Route:
    def __init__(self):
        self.head = None                   # Initialize the head attribute to None

    def add_waypoint(self, location, description):
        new_waypoint = Waypoint(location, description)  # Create a new Waypoint object
        if self.head is None:
            self.head = new_waypoint                   # If the route is empty, set the head to the new waypoint
        else:
            current = self.head                        # Traverse to the end of the route
            while current.next:
                current = current.next
            current.next = new_waypoint                # Add the new waypoint at the end
            new_waypoint.prev = current

    def insert_waypoint_after(self, target, location, description):
        new_waypoint = Waypoint(location, description)  # Create a new Waypoint object
        current = self.head
        while current:
            if current.location == target:
                new_waypoint.next = current.next          # Insert the new waypoint after the target waypoint
                current.next = new_waypoint
                new_waypoint.prev = current
                if new_waypoint.next:
                    new_waypoint.next.prev = new_waypoint  # Update the previous reference of the next waypoint
                break
            current = current.next

    def remove_waypoint(self, location):
        current = self.head
        if current and current.location == location:
            self.head = current.next                     # Remove the first waypoint if it matches the location
            if self.head:
                self.head.prev = None
            return
        while current:
            if current.location == location:
                if current.next:
                    current.next.prev = current.prev       # Update the previous reference of the next waypoint
                if current.prev:
                    current.prev.next = current.next       # Update the next reference of the previous waypoint
                break
            current = current.next

    def traverse_forward(self):
        current = self.head
        while current:
            print(f"Your current Location is: {current.location}, Description: {current.description}")
            current = current.next                     # Traverse the route forward

# Define a subclass BidirectionalRoute, inheriting from the Route class
class BidirectionalRoute(Route):
    def traverse_backward(self):
        current = self.head
        while current and current.next:
            current = current.next
        while current:
            print(f"Your current Location is : {current.location}, Description: {current.description}")
            current = current.prev                     # Traverse the route backward

# Test scenario
if __name__ == '__main__':
    route = BidirectionalRoute()
    route.add_waypoint("Mukono", "Bishop_Stage")
    route.add_waypoint("Kampala", "Koki_towers")
    route.add_waypoint("Nansana", "Kumastowa")
    route.traverse_forward()                          # Display the waypoints in forward order
    route.insert_waypoint_after("Mukono", "Namasuba", "Freedom_city")  # Insert a waypoint after "Mukono"
    route.remove_waypoint('Mukono')                   # Remove the waypoint with location "Mukono"
    route.traverse_backward()                         # Display the waypoints in backward order
