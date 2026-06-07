"use client";

import { useEffect, useState } from "react";
import { getTopGrowth } from "@/lib/api";

interface Channel {
  channel_name: string;
  growth_score: number;
}

export default function TopGrowth() {
  const [channels, setChannels] = useState<Channel[]>([]);

  useEffect(() => {
    getTopGrowth().then(setChannels);
  }, []);

  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
      <h2 className="mb-6 text-2xl font-semibold">
        Top Growth Channels
      </h2>

      <div className="space-y-3">
        {channels.map((channel, index) => (
          <div
            key={index}
            className="flex justify-between rounded-xl border border-white/10 p-3"
          >
            <span>{channel.channel_name}</span>

            <span className="font-bold text-green-400">
              {channel.growth_score}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}