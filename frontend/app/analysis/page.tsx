"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { getAIReview } from "@/lib/api";

export default function AnalysisPage() {
  const [channel, setChannel] = useState("");
  const [review, setReview] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const analyzeChannel = async () => {
    if (!channel) return;

    setLoading(true);
    setError("");

    try {
  const result = await getAIReview(channel);

  console.log("AI Review Result:", result);

  setReview(result);
} catch (err) {
  console.error("AI Review Error:", err);

  setError("Failed to generate analysis");
} finally {
  setLoading(false);
}
  };

  return (
    <main className="min-h-screen bg-black px-6 py-20 text-white">
      <div className="mx-auto max-w-5xl">

        <h1 className="mb-3 text-5xl font-bold">
          Channel Analysis
        </h1>

        <p className="mb-10 text-zinc-400">
          Analyze any creator and generate an AI-powered review.
        </p>

        <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
          <div className="flex flex-col gap-4 md:flex-row">

            <input
              value={channel}
              onChange={(e) => setChannel(e.target.value)}
              placeholder="Enter channel name..."
              className="flex-1 rounded-xl border border-white/10 bg-black px-4 py-3 outline-none"
            />

            <Button
              onClick={analyzeChannel}
              disabled={loading}
            >
              {loading
                ? "Generating..."
                : "Analyze"}
            </Button>

            <Button
              variant="outline"
              onClick={() =>
                window.open(
                  `http://127.0.0.1:8000/report/${channel}`,
                  "_blank"
                )
              }
            >
              Export PDF
            </Button>

          </div>
        </div>

        {error && (
          <div className="mt-4 rounded-xl border border-red-500/20 bg-red-500/10 p-4 text-red-300">
            {error}
          </div>
        )}

        {review && (
          <div className="mt-8 rounded-2xl border border-white/10 bg-white/5 p-6">
            <h2 className="mb-4 text-2xl font-semibold">
              AI Review
            </h2>

            <div className="prose prose-invert max-w-none">
              <p className="leading-8 text-zinc-300">
                {typeof review === "string"
                  ? review
                  : review.review}
              </p>
            </div>
          </div>
        )}

      </div>
    </main>
  );
}