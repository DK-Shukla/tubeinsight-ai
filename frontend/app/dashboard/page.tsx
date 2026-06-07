import TopHealth from "@/components/top-health";
import TopGrowth from "@/components/top-growth";

export default function DashboardPage() {
  return (
    <main className="min-h-screen bg-black p-8 text-white">
      <div className="mx-auto max-w-7xl">
        <h1 className="mb-2 text-5xl font-bold">
          Dashboard
        </h1>

        <p className="mb-12 text-zinc-400">
          Creator intelligence at a glance.
        </p>

        {/* Stats Cards */}
        <div className="grid gap-6 md:grid-cols-4">
          <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
            <h3 className="text-sm text-zinc-500">
              Channels
            </h3>

            <p className="mt-2 text-4xl font-bold">
              296
            </p>
          </div>

          <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
            <h3 className="text-sm text-zinc-500">
              AI Reviews
            </h3>

            <p className="mt-2 text-4xl font-bold">
              1000+
            </p>
          </div>

          <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
            <h3 className="text-sm text-zinc-500">
              Genres
            </h3>

            <p className="mt-2 text-4xl font-bold">
              11
            </p>
          </div>

          <div className="rounded-2xl border border-white/10 bg-white/5 p-6">
            <h3 className="text-sm text-zinc-500">
              APIs
            </h3>

            <p className="mt-2 text-4xl font-bold">
              7
            </p>
          </div>
        </div>

        {/* Top Health Channels */}
        <div className="mt-10 grid gap-6 lg:grid-cols-2">
      <TopHealth />
      <TopGrowth />
      </div>
      </div>
    </main>
  );
}