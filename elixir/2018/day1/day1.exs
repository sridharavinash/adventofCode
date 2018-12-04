defmodule Day1 do
  def part1(filename) do
    File.stream!(filename)
    |> Stream.map(fn line ->
      {integer,_} = Integer.parse(line)
      integer
    end)
    |> Enum.sum()
  end

  def part2(filename) do
    File.stream!(filename)
    |> Stream.map(fn line ->
      {integer,_} = Integer.parse(line)
      integer
    end)
    |> Stream.cycle()
    |> Enum.reduce_while({0,%{}}, fn x, {curr, seen} ->
      new = curr + x
      if Map.has_key?(seen,new) do
        {:halt, new}
      else
        seen = Map.put(seen,new,true)
        {:cont, {new, seen}}
      end
    end)
  end
end

Day1.part1("input.txt") |> IO.puts
Day1.part2("input.txt") |> IO.puts
