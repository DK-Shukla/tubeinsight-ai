"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { getCompetitorReview } from "@/lib/api";

export default function CompetitorPage() {
  const [channel1, setChannel1] = useState("");
  const [channel2, setChannel2] = useState("");

  const [result, setResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const compareChannels = async () => {
    if (!channel1 || !channel2) return;

    setLoading(true);

    try {
      const data = await getCompetitorReview(
        channel1,
        channel2
      );

      setResult(data);
    } catch (error) {
      console.error(error);
    }

    setLoading(false);
  };

  return (
    <main className="min-h-screen bg-black px-6 py-20 text-white">
      <div className="mx-auto max-w-5xl">

        <h1 className="mb-3 text-5xl font-bold">
          Competitor Analysis
        </h1>

        <p className="mb-10 text-zinc-400">
          Compare two creators using AI.
        </p>

        <div className="rounded-2xl border border-white/10 bg-white/5 p-6">

          <div className="grid gap-4 md:grid-cols-2">

            <input
              value={channel1}
              onChange={(e) =>
                setChannel1(e.target.value)
              }
              placeholder="Channel 1"
              className="rounded-xl border border-white/10 bg-black px-4 py-3 outline-none"
            />

            <input
              value={channel2}
              onChange={(e) =>
                setChannel2(e.target.value)
              }
              placeholder="Channel 2"
              className="rounded-xl border border-white/10 bg-black px-4 py-3 outline-none"
            />

          </div>

          <Button
            className="mt-4"
            onClick={compareChannels}
          >
            {loading
              ? "Comparing..."
              : "Compare"}
          </Button>

        </div>

        {result && (
          <div className="mt-8 rounded-2xl border border-white/10 bg-white/5 p-6">

            <h2 className="mb-4 text-2xl font-semibold">
              AI Competitor Review
            </h2>

            <pre className="whitespace-pre-wrap text-zinc-300">
              {typeof result === "string"
                ? result
                : result.review ||
                  JSON.stringify(
                    result,
                    null,
                    2
                  )}
            </pre>

          </div>
        )}

      </div>
    </main>
  );
}