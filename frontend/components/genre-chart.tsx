"use client";

import { useEffect, useState } from "react";
import { getGenreAnalysis } from "@/lib/api";

import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

interface GenreData {
  genre: string;
  total_channels: number;
  avg_health_score: number;
  avg_growth_score: number;
}

export default function GenreChart() {
const [data, setData] = useState<GenreData[]>([]);
const [loading, setLoading] = useState(true);
  useEffect(() => {
  const fetchData = async () => {
    try {
      const result = await getGenreAnalysis();

      result.sort(
        (a: GenreData, b: GenreData) =>
          b.avg_growth_score - a.avg_growth_score
      );

      setData(result);
    } catch (error) {
      console.error(error);
    }
  };

  fetchData();
}, []);

  return (
    <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
      <h2 className="mb-6 text-2xl font-semibold">
        Genre Intelligence
      </h2>



      <div className="h-112.5">
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />

            <XAxis
         dataKey="genre"
         angle={-25}
            textAnchor="end"
          height={80}
         tick={{ fill: "#a1a1aa" }}
/>

            <YAxis
              tick={{ fill: "#a1a1aa" }}
            />

<Tooltip
  contentStyle={{
    backgroundColor: "#09090b",
    border: "1px solid #27272a",
    borderRadius: "12px",
  }}
/>
            <Bar
              dataKey="avg_growth_score"
              fill="#22d3ee"
              radius={[4, 4, 0, 0]}
            />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}