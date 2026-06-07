export default function Stats() {
  const stats = [
    {
      value: "296+",
      label: "Channels Tracked",
    },
    {
      value: "1,000+",
      label: "Insights Generated",
    },
    {
      value: "7",
      label: "Analysis Modules",
    },
    {
      value: "24/7",
      label: "Available",
    },
  ];

  return (
    <section className="py-20">
      <div className="mx-auto grid max-w-6xl grid-cols-2 gap-8 md:grid-cols-4">
        {stats.map((stat) => (
          <div
            key={stat.label}
            className="text-center"
          >
            <h3 className="text-5xl font-bold">
              {stat.value}
            </h3>

            <p className="mt-2 text-zinc-500">
              {stat.label}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}