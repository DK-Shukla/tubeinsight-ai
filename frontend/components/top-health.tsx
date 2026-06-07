"use client";

import { useEffect, useState } from "react";
import { getTopHealth } from "@/lib/api";

interface Channel {
  channel_name: string;
  health_score: number;
}

export default function TopHealth() {
  const [channels, setChannels] = useState<Channel[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getTopHealth()
      .then((data) => {
        setChannels(data);
      })
      .catch((error) => {
        console.error(error);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
      <h2 className="mb-6 text-2xl font-semibold">
        Top Health Channels
      </h2>

      {loading ? (
        <p className="text-zinc-400">
          Loading...
        </p>
      ) : (
        <div className="space-y-3">
          {channels.map((channel, index) => (
            <div
              key={index}
              className="flex items-center justify-between rounded-xl border border-white/10 p-3"
            >
              <span className="font-medium">
                {channel.channel_name}
              </span>

              <span className="text-cyan-400 font-bold">
                {channel.health_score}
              </span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}