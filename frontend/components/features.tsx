import {
  Card,
  CardContent,
} from "@/components/ui/card";

export default function Features() {
  const features = [
    {
      title: "Channel Review",
      desc: "See strengths, weaknesses and growth opportunities.",
    },
    {
      title: "Competitor Breakdown",
      desc: "Compare creators side by side.",
    },
    {
      title: "Genre Trends",
      desc: "Discover where attention is moving.",
    },
  ];

  return (
    <section
      id="features"
      className="py-32"
    >
      <div className="mx-auto max-w-6xl">
        <h2 className="mb-16 text-center text-5xl font-bold">
          Everything you need
        </h2>

        <div className="grid gap-8 md:grid-cols-3">
          {features.map((feature) => (
            <Card
              key={feature.title}
              className="border-white/10 bg-white/5"
            >
              <CardContent className="p-8">
                <h3 className="mb-4 text-2xl font-semibold">
                  {feature.title}
                </h3>

                <p className="text-zinc-400">
                  {feature.desc}
                </p>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}