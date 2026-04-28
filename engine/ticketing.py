import datetime
import uuid

def generate_ticket(node_id, detection_results, coordinates):
    """
    Simulates the creation of a Gov-Tech maintenance ticket.
    """
    ticket_id = f"TR-BK-{str(uuid.uuid4())[:8].upper()}" # Unique ID
    
    ticket_data = {
        "Ticket ID": ticket_id,
        "Timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Location": f"{coordinates['lat']}, {coordinates['lng']}",
        "Criticality": "High" if detection_results['confidence'] > 85 else "Medium",
        "Detection Summary": f"AI verified {detection_results['label']} with {detection_results['confidence']}% confidence.",
        "Status": "OPEN - Dispatched to Ward Maintenance"
    }
    
    return ticket_data
