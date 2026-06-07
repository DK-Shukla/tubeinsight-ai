import Navbar from "@/components/navbar";
import Stats from "@/components/stats";
import Features from "@/components/features";
import DashboardPreview from "@/components/dashboard-preview";
import { Button } from "@/components/ui/button";
import GenreChart from "@/components/genre-chart";

export default function Home() {
  return (
    <main className="relative min-h-screen overflow-hidden bg-black text-white">
      {/* Background Glow */}
      <div className="fixed inset-0 -z-10 overflow-hidden">
        <div className="absolute left-1/4 top-20 h-125 w-125 rounded-full bg-cyan-500/15 blur-[120px]" />
        <div className="absolute right-1/4 top-40 h-125 w-125 rounded-full bg-violet-500/15 blur-[120px]" />
      </div>

      <Navbar />

      {/* Hero Section */}
      <section className="flex min-h-screen flex-col items-center justify-center px-6 pt-20 text-center">
        <div className="mb-6 rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-zinc-400 backdrop-blur-sm">
          Creator Analytics Platform
        </div>

        <h1 className="max-w-6xl text-6xl font-bold tracking-tight md:text-8xl">
          See your channel
          <span className="block bg-linear-to-r from-cyan-400 via-blue-500 to-violet-500 bg-clip-text text-transparent">
            through a different lens.
          </span>
        </h1>

        <p className="mt-8 max-w-3xl text-lg text-zinc-400 md:text-xl">
          Understand what separates fast-growing channels from the rest.
          Compare creators, spot trends, and discover opportunities you
          might otherwise miss.
        </p>

        <div className="mt-10 flex flex-col gap-4 sm:flex-row">
          <Button size="lg">
            Explore Dashboard
          </Button>

          <Button
            variant="outline"
            size="lg"
          >
            Try a Channel Review
          </Button>
        </div>

        {/* Product Preview */}
        <div className="mt-20 w-full max-w-5xl rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-xl">
          <div className="grid gap-6 md:grid-cols-3">
            <div className="rounded-xl border border-white/10 bg-black/40 p-6">
              <h3 className="mb-3 text-lg font-semibold">
                Top Channels
              </h3>

              <div className="space-y-2 text-zinc-400">
                <p>T-Series</p>
                <p>MrBeast</p>
                <p>PewDiePie</p>
              </div>
            </div>

            <div className="rounded-xl border border-white/10 bg-black/40 p-6">
              <h3 className="mb-3 text-lg font-semibold">
                Growth Score
              </h3>

              <p className="text-5xl font-bold text-cyan-400">
                71.7
              </p>

              <p className="mt-2 text-sm text-zinc-500">
                Above industry average
              </p>
            </div>

            <div className="rounded-xl border border-white/10 bg-black/40 p-6">
              <h3 className="mb-3 text-lg font-semibold">
                AI Review
              </h3>

              <p className="text-zinc-400">
                Strong audience retention, consistent uploads,
                and high long-term growth potential.
              </p>
            </div>
          </div>
        </div>
           </section>

      {/* Genre Intelligence Section */}
      <section className="px-6 py-20">
        <div className="mx-auto max-w-7xl">
          <div className="mb-10 text-center">
            <h2 className="text-4xl font-bold">
              Genre Intelligence
            </h2>

            <p className="mt-4 text-zinc-400">
              Discover which YouTube categories are growing
              the fastest using real channel performance data.
            </p>
          </div>

          <GenreChart />
        </div>
      </section>

      {/* Statistics */}
      <Stats />

      {/* Features */}
      <Features />

      {/* Dashboard Preview */}
      <DashboardPreview />
    </main>
  );
}