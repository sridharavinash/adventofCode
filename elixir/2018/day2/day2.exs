defmodule Day2 do
  def readFile(filename) do
    File.stream!(filename)
    |> Stream.map(&String.trim/1)
    |> Stream.map(&String.graphemes/1)
    |> Enum.take(2)
    |>Enum.reduce(%{}, fn x, acc -> Map.update(acc, x, 1, &(&1 + 1)) end)
  end

end

IO.puts Day2.readFile("input.txt")


