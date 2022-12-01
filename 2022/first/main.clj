(require '[clojure.string :as str])

(defn main []
(def elfs (str/split (slurp "calories.txt") #"\n\r\n\r"))
(def sums (for [elf elfs] (apply + (map #(Integer/parseInt %) (str/split elf #"\n\r")))))
(println (apply max sums))
)

(main)