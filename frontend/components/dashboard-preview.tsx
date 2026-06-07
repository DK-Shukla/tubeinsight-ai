export default function DashboardPreview() {
  return (
    <section
      id="preview"
      className="px-6 py-32"
    >
      <div className="mx-auto max-w-7xl">
        <div className="mb-16 text-center">
          <h2 className="text-5xl font-bold">
            Built for creators who care about growth
          </h2>

          <p className="mt-4 text-zinc-400">
            Understand performance, compare competitors,
            and uncover opportunities in seconds.
          </p>
        </div>

        <div className="rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-xl">
          <div className="grid gap-6 lg:grid-cols-3">

            <div className="rounded-2xl border border-white/10 bg-black/40 p-6">
              <h3 className="mb-4 text-lg font-semibold">
                Top Health Channels
              </h3>

              <div className="space-y-3">
                <div className="flex justify-between">
                  <span>T-Series</span>
                  <span>65.9</span>
                </div>

                <div className="flex justify-between">
                  <span>SET India</span>
                  <span>45.3</span>
                </div>

                <div className="flex justify-between">
                  <span>MrBeast</span>
                  <span>28.6</span>
                </div>
              </div>
            </div>

            <div className="rounded-2xl border border-white/10 bg-black/40 p-6">
              <h3 className="mb-4 text-lg font-semibold">
                Growth Analysis
              </h3>

              <div className="space-y-4">
                <div>
                  <p className="text-sm text-zinc-500">
                    Growth Score
                  </p>

                  <p className="text-5xl font-bold text-cyan-400">
                    71.7
                  </p>
                </div>

                <div className="h-2 rounded-full bg-zinc-800">
                  <div className="h-2 w-[72%] rounded-full bg-cyan-400" />
                </div>
              </div>
            </div>

            <div className="rounded-2xl border border-white/10 bg-black/40 p-6">
              <h3 className="mb-4 text-lg font-semibold">
                Channel Review
              </h3>

              <p className="text-zinc-400">
                Strong growth trajectory with high engagement.
                Consistent publishing pattern supports
                long-term audience retention.
              </p>
            </div>

          </div>
        </div>
      </div>
    </section>
  );
}