def calculate_integrity(ward_name):
    """
    Calculates the Infrastructure Integrity Score based on 
    Topographical Logic vs. Physical Reality.
    """
    # Mock data - in production, these would be results from your GIS queries
    data_points = {
        "Hebbal Valley": {"logic": 0.85, "vulnerability": 0.70, "ai_clearance": 0.65},
        "Koramangala": {"logic": 0.40, "vulnerability": 0.30, "ai_clearance": 0.20},
        "Varthur": {"logic": 0.60, "vulnerability": 0.55, "ai_clearance": 0.50}
    }
    
    stats = data_points.get(ward_name, {"logic": 0, "vulnerability": 0, "ai_clearance": 0})
    
    # Apply Weights
    w1, w2, w3 = 0.50, 0.20, 0.30
    
    score = (stats['logic'] * w1) + (stats['vulnerability'] * w2) + (stats['ai_clearance'] * w3)
    
    return round(score * 100, 1)
