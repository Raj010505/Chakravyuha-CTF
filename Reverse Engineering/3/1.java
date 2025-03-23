import java.util.Base64;
import java.util.Scanner;

class 1 {
    private final String hello = "5375706572536563757265313233";
    private final String[] randomInt = new String[]{"47", "38", "4B", "45", "59", "7B", "41", "72", "69", "73", "65", "5F", "4D", "79", "5F", "53", "68", "61", "64", "6F", "77", "73", "21", "7D"};

    private String decodeHexString(String var1) {
        StringBuilder var2 = new StringBuilder();
        for (int var3 = 0; var3 < var1.length(); var3 += 2) {
            var2.append((char) Integer.parseInt(var1.substring(var3, var3 + 2), 16));
        }
        return var2.toString();
    }

    private String error1() { 
        return this.decodeHexString(String.join("", this.randomInt));
    }

    private String error2() { 
        return Base64.getEncoder().encodeToString(this.error1().getBytes());
    }

    public boolean verifyAccess(String var1) {
        return var1.equals(this.decodeHexString(hello));
    }

    public static void main(String[] var0) {
        VaultDoorTraining var1 = new VaultDoorTraining();
        Scanner var2 = new Scanner(System.in);
        System.out.print("Enter vault key: ");
        String var3 = var2.next();
        if (var1.verifyAccess(var3)) {
            System.out.println("Access granted.");
            System.out.println("Hmm... You came all this way, and for what? 🫤");
            System.out.println("Just an empty vault... No treasure, no secrets, nothing.");
            System.out.println("Why did you even try? Was it worth it? 🥀");
            System.out.println("Perhaps all along, the real flag was the friends we made along the way. 😔");
            System.out.println("...");
            System.out.println("Error Code: " + var1.error2());
        } else {
            System.out.println("Access denied!");
        }
    }
}
