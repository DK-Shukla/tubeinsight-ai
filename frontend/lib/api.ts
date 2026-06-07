const API_BASE_URL = "http://127.0.0.1:8000";

// ======================
// Top Health Channels
// ======================
export async function getTopHealth() {
  const response = await fetch(
    `${API_BASE_URL}/top-health`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch Top Health data");
  }

  return response.json();
}

// ======================
// Top Growth Channels
// ======================
export async function getTopGrowth() {
  const response = await fetch(
    `${API_BASE_URL}/top-growth`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch Top Growth data");
  }

  return response.json();
}

// ======================
// Genre Analysis
// ======================
export async function getGenreAnalysis() {
  const response = await fetch(
    `${API_BASE_URL}/genre-analysis`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch Genre Analysis");
  }

  return response.json();
}

// ======================
// AI Channel Review
// ======================
export async function getAIReview(
  channelName: string
) {
  const response = await fetch(
    `${API_BASE_URL}/ai/channel-review/${encodeURIComponent(
      channelName
    )}`
  );

  if (!response.ok) {
    throw new Error("Failed to fetch AI Review");
  }

  return response.json();
}

// ======================
// AI Competitor Review
// ======================
export async function getCompetitorReview(
  channel1: string,
  channel2: string
) {
  const response = await fetch(
    `${API_BASE_URL}/ai/competitor-review/${encodeURIComponent(
      channel1
    )}/${encodeURIComponent(channel2)}`
  );

  if (!response.ok) {
    throw new Error(
      "Failed to fetch Competitor Review"
    );
  }

  return response.json();
}




export async function getGrowthStrategy(
  channelName: string
) {
  const response = await fetch(
    `${API_BASE_URL}/ai/growth-strategy/${encodeURIComponent(
      channelName
    )}`
  );

  if (!response.ok) {
    throw new Error(
      "Failed to fetch Growth Strategy"
    );
  }

  return response.json();
}