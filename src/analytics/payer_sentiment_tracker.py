"""Track payer sentiment and coverage decisions."""

class PayerSentimentTracker:
    """Monitor payer sentiment and market access decisions."""
    
    SENTIMENT_SCORES = {"Positive": 5, "Neutral": 3, "Negative": 1}
    
    def __init__(self):
        self.payers = {}
    
    def add_payer_assessment(self, payer_name: str, 
                            sentiment: str, coverage_status: str,
                            comment: str = "") -> None:
        """
        Add payer sentiment assessment.
        Args:
            payer_name: Payer organization name
            sentiment: One of Positive/Neutral/Negative
            coverage_status: Covered/Limited/Not Covered/Pending
            comment: Optional assessment comment
        """
        if sentiment not in self.SENTIMENT_SCORES:
            raise ValueError(f"Invalid sentiment: {sentiment}")
        
        valid_statuses = ["Covered", "Limited", "Not Covered", "Pending"]
        if coverage_status not in valid_statuses:
            raise ValueError(f"Invalid coverage status: {coverage_status}")
        
        self.payers[payer_name] = {
            'sentiment': sentiment,
            'sentiment_score': self.SENTIMENT_SCORES[sentiment],
            'coverage_status': coverage_status,
            'comment': comment
        }
    
    def get_coverage_summary(self) -> dict:
        """Get coverage distribution across payers."""
        summary = {
            "Covered": 0,
            "Limited": 0,
            "Not Covered": 0,
            "Pending": 0
        }
        
        for payer_data in self.payers.values():
            summary[payer_data['coverage_status']] += 1
        
        return summary
    
    def get_average_sentiment_score(self) -> float:
        """Calculate average sentiment score across all payers."""
        if not self.payers:
            return 0.0
        
        total_score = sum(p['sentiment_score'] for p in self.payers.values())
        return total_score / len(self.payers)
