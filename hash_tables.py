import java.util.HashMap;
import java.util.Map;

public class table {
    public int[] Alteracao_HashMap(int[] numero, int numerador) {
        Map<Integer, Integer> mapaTable = new HashMap<>();

        for (int p = 0; p < numero.length; p++) {
            mapaTable.put(numero[p], p);
        }

        for (int k = 0; k < numero.length; k++) {
            int auxiliar = numerador - numero[k];
            if (mapaTable.containsKey(auxiliar) && mapaTable.get(auxiliar) != k) {
                return new int[]{k, mapaTable.get(auxiliar)};
            }
        }
        return null;
    }
}
