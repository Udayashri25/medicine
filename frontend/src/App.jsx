"use client"

import { useState } from "react"
import axios from "axios"
import "./App.css"

const BACKEND_URL = "http://localhost:8000" // Change for deployment

export default function App() {
  const [dataset, setDataset] = useState("General Medical")
  const [text, setText] = useState("")
  const [medicines, setMedicines] = useState([])
  const [medicineImages, setMedicineImages] = useState({})
  const [sentiment, setSentiment] = useState(null)
  const [loading, setLoading] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!text.trim()) return

    setLoading(true)
    setMedicines([])
    setMedicineImages({})
    setSentiment(null)

    try {
      const res = await axios.post(`${BACKEND_URL}/analyze`, {
        text,
        dataset,
      })

      const { medicines, sentiment, audio_url } = res.data
      setMedicines(medicines || [])
      setSentiment(sentiment)

      // Fetch images for each medicine
      if (medicines && medicines.length > 0) {
        const images = {}
        await Promise.all(
          medicines.map(async (med) => {
            try {
              const imgRes = await axios.get(
                `${BACKEND_URL}/image?medicine_name=${encodeURIComponent(med)}`
              )
              images[med] = imgRes.data.url || null
            } catch {
              images[med] = null
            }
          })
        )
        setMedicineImages(images)
      }

      // Play voice
      if (audio_url) {
        const audio = new Audio(`${BACKEND_URL}${audio_url}`)
        audio.play().catch((err) => console.log("Audio playback failed:", err))
      }
    } catch (err) {
      console.error("Analysis failed:", err)
    }
    setLoading(false)
  }

  const getSentimentClass = (score) => {
    if (score > 0.2) return "sentiment-positive"
    if (score < -0.2) return "sentiment-negative"
    return "sentiment-neutral"
  }

  const getSentimentLabel = (score) => {
    if (score > 0.2) return "Positive"
    if (score < -0.2) return "Negative"
    return "Neutral"
  }

  return (
    <div className="app-container">
      {/* Header */}
      <header className="header">
        <div className="header-icon" style={{ fontSize: "4rem" }}>🩺</div>
        <h1 className="main-title">Medicine.io</h1>
        <p className="subtitle">AI-Powered Medicine Recommender</p>
      </header>

      {/* Form */}
      <div className="form-container">
        <form onSubmit={handleSubmit} className="form-section">
          <select value={dataset} onChange={(e) => setDataset(e.target.value)} className="form-select">
            <option value="General Medical">General Medical</option>
            <option value="Mental Health">Mental Health</option>
            <option value="Pediatric">Pediatric</option>
            <option value="Geriatric">Geriatric</option>
            <option value="Dermatological">Dermatological</option>
            <option value="Cardiovascular">Cardiovascular</option>
            <option value="Gastrointestinal">Gastrointestinal</option>
            <option value="Neurological">Neuroligical</option>
            <option value="Respiratory">Respiratory</option>
          </select>

          <input
            type="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Describe your symptoms in detail..."
            className="form-input"
            disabled={loading}
          />

          <button
            type="submit"
            className={`submit-button ${loading ? "loading" : ""}`}
            disabled={loading || !text.trim()}
          >
            {loading ? (
              <>
                <span className="loading-spinner"></span>
                <span style={{ marginLeft: "8px" }}>Analyzing...</span>
              </>
            ) : (
              "Analyze"
            )}
          </button>
        </form>
      </div>

      {/* Sentiment Display */}
      {sentiment !== null && (
        <div className="sentiment-container">
          <div className={`sentiment-badge ${getSentimentClass(sentiment)}`}>
            {getSentimentLabel(sentiment)} Sentiment: {sentiment.toFixed(2)}
          </div>
        </div>
      )}

      {/* Results */}
      <div className="results-container">
        {medicines.length > 0 ? (
          <>
            <h2 className="results-title">Recommended Medicines</h2>
            <div className="medicines-grid">
              {medicines.map((med, idx) => (
                <div key={idx} className="medicine-card">
                  <h3 className="medicine-name">{med}</h3>
                  <div className="medicine-image-container">
                    {medicineImages[med] ? (
                      <img
                        src={medicineImages[med]}
                        alt={`${med} medicine`}
                        className="medicine-image"
                      />
                    ) : (
                      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100%", color: "#64748b" }}>
                        <div style={{ fontSize: "3rem", marginBottom: "0.5rem" }}>💊</div>
                        <div style={{ fontSize: "0.9rem" }}>Image not available</div>
                      </div>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </>
        ) : (
          !loading &&
          text && (
            <div className="empty-state">
              <div className="empty-state-icon">🔍</div>
              <p className="empty-state-text">Enter your symptoms above to get personalized medicine recommendations</p>
            </div>
          )
        )}
      </div>
    </div>
  )
}
