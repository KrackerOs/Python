import { useState } from "react";
import {
  Dimensions,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from "react-native";

const App = () => {
  const [message, setMessage] = useState("");

  const handlePress = () => {
    setMessage("Você começou a aula!");
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>
        Essa é sua aula de Programação Mobile
      </Text>
      <Text style={styles.subtitle}>
        Clique no botão abaixo
      </Text>
      <TouchableOpacity
        style={styles.button}
        onPress={handlePress}
      >
        <Text style={styles.buttonText}>
          COMEÇAR
        </Text>
      </TouchableOpacity>
      {message !== "" && (
        <Text style={styles.message}>
          {message}
        </Text>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#7067aF",
    alignItems: "center",
    justifyContent: "center",
    padding: 20,
  },
  title: {
    fontSize: 30,
    fontWeight: "bold",
    color: "#71c9f1",
    textAlign: "center",
    marginBottom: 28,
  },
  subtitle: {
    fontSize: 18,
    color: "#2865b1",
    textAlign: "center",
    marginBottom: 40,
  },
  button: {
    backgroundColor: "#088808",
    paddingVertical: 18,
    paddingHorizontal: 50,
    borderRadius: 20,
  },
  buttonText: {
    color: "#FFFFFF",
    fontSize: 20,
    fontWeight: "bold",
  },
  message: {
    marginTop: 40,
    fontSize: 24,
    color: "#FACC15",
    fontWeight: "bold",
    textAlign: "center",
  },
});

export default App;