from core.models import Airport, AirportRoute
from django.db.models import Max


def find_nth_route_node(start_airport: Airport, position: str, n: int):
    """
    Utility function that returns:
        (final_airport, path_list, error_message)
    """
    if not isinstance(n, int) or n <= 0:
        return None, [], "N must be a positive integer."

    if not start_airport:
        return None, [], "Starting airport is required."

    if position not in ("Left", "Right"):
        return None, [], "Position must be either 'Left' or 'Right'."  # Fixed case sensitivity

    current = start_airport
    path = [current.code]
    visited = set([current.id])  # cycle detection

    # ----------- Main traversal loop -----------
    for step in range(1, n + 1):
        try:
            route = (
                AirportRoute.objects
                .filter(from_airport=current, position=position)
                .select_related("to_airport")
                .order_by('duration')
                .first()
            )

            if not route:
                error_msg = (
                    f"No '{position}' route found from '{current.code}' "
                    f"at step {step} of {n}."
                )
                return None, path, error_msg

            current = route.to_airport
            path.append(current.code)

            # ----------- Detect cycles -----------
            if current.id in visited:
                return current, path, (
                    f"Cycle detected at '{current.code}'. "
                    f"Traversal stopped to prevent infinite loop."
                )

            visited.add(current.id)

        except Exception as e:
            return None, path, f"Error during traversal: {str(e)}"

    return current, path, None




def get_longest_node_from_airport(start_airport):
    """
    Returns all AirportRoutes with the maximum duration
    starting from the given airport.
    """
    if not start_airport:
        return []

    # Find the maximum duration
    max_duration = (
        AirportRoute.objects
        .filter(from_airport=start_airport)
        .aggregate(Max('duration'))['duration__max']
    )

    if max_duration is None:
        return []

    # Get all routes with the maximum duration
    routes = (
        AirportRoute.objects
        .select_related('from_airport', 'to_airport')
        .filter(from_airport=start_airport, duration=max_duration)
    )
    return routes



def get_shortest_node(from_airport, to_airport):
    """
    Returns the AirportRoute with the shortest duration between
    the given from_airport and to_airport.
    """
    if not from_airport or not to_airport:
        return None

    route = (
        AirportRoute.objects
        .select_related('from_airport', 'to_airport')
        .filter(from_airport=from_airport, to_airport=to_airport)
        .order_by('duration')
        .first()
    )
    return route
