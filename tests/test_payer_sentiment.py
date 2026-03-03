import pytest
from src.analytics.payer_sentiment_tracker import PayerSentimentTracker

def test_add_payer_assessment():
    tracker = PayerSentimentTracker()
    tracker.add_payer_assessment("Aetna", "Positive", "Covered")
    assert "Aetna" in tracker.payers
    assert tracker.payers["Aetna"]["sentiment"] == "Positive"

def test_invalid_sentiment():
    tracker = PayerSentimentTracker()
    with pytest.raises(ValueError):
        tracker.add_payer_assessment("Aetna", "Unknown", "Covered")

def test_invalid_coverage_status():
    tracker = PayerSentimentTracker()
    with pytest.raises(ValueError):
        tracker.add_payer_assessment("Aetna", "Positive", "Invalid")

def test_coverage_summary():
    tracker = PayerSentimentTracker()
    tracker.add_payer_assessment("Aetna", "Positive", "Covered")
    tracker.add_payer_assessment("UnitedHealth", "Neutral", "Limited")
    tracker.add_payer_assessment("Humana", "Negative", "Not Covered")
    
    summary = tracker.get_coverage_summary()
    assert summary["Covered"] == 1
    assert summary["Limited"] == 1
    assert summary["Not Covered"] == 1
    assert summary["Pending"] == 0

def test_average_sentiment():
    tracker = PayerSentimentTracker()
    tracker.add_payer_assessment("Aetna", "Positive", "Covered")  # 5
    tracker.add_payer_assessment("UnitedHealth", "Neutral", "Limited")  # 3
    
    avg = tracker.get_average_sentiment_score()
    assert avg == 4.0  # (5 + 3) / 2
