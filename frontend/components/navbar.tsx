import Link from "next/link";
import Image from "next/image";
import { Button } from "@/components/ui/button";

export default function Navbar() {
  return (
    <nav className="fixed top-0 z-50 w-full border-b border-white/10 bg-black/60 backdrop-blur-xl">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">

        {/* Logo + Brand */}
        <Link href="/" className="flex items-center gap-3">
          <Image
            src="/logo.jpeg"
            alt="TubeInsight Logo"
            width={42}
            height={42}
            className="rounded-xl border border-white/10 shadow-lg"
            priority
          />

          <div>
            <h1 className="bg-linear-to-r from-cyan-400 to-violet-500 bg-clip-text text-xl font-bold text-transparent">
              TubeInsight
            </h1>

            <p className="text-xs text-zinc-500">
              Creator Intelligence
            </p>
          </div>
        </Link>

        {/* Navigation */}
        <div className="hidden items-center gap-8 md:flex">
          <Link
            href="/"
            className="text-zinc-400 transition hover:text-white"
          >
            Home
          </Link>

          <Link
            href="/analysis"
            className="text-zinc-400 transition hover:text-white"
          >
            Analysis
          </Link>

          <Link
            href="/competitor"
            className="text-zinc-400 transition hover:text-white"
          >
            Competitor
          </Link>

          <a
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
            className="text-zinc-400 transition hover:text-white"
          >
            GitHub
          </a>
        </div>

        {/* CTA Button */}
        <Link href="/analysis">
          <Button className="bg-cyan-500 text-black hover:bg-cyan-400">
            Start Analysis
          </Button>
        </Link>

      </div>
    </nav>
  );
}