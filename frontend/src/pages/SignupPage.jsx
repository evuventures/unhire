import React, { useState } from "react";
import {
  Box,
  Card,
  TextField,
  Button,
  Typography,
  IconButton,
  InputAdornment,
} from "@mui/material";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";

export default function SignupPage() {
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);

  return (
    <Box
      sx={{
        bgcolor: "#f9f9f9",       // full page background
        minHeight: "100vh",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
       bgcolor: "#f9f9f9",   // ✅ background ONLY here
      }}
    >
      <Card
        sx={{
          width: "100%",
          maxWidth: 400,
          p: 5,
          borderRadius: "16px",
          boxShadow: 4,
          bgcolor: "#f0efef",     // card background
        }}
      >
        {/* Top logo placeholder */}
        <Box sx={{ display: "flex", justifyContent: "flex-start", mb: 3 }}>
          <Box
            sx={{
              width: 40,
              height: 40,
              bgcolor: "#C49AF2",
              borderRadius: "50%",
            }}
          />
        </Box>

        {/* Branded logo placeholder */}
        <Box sx={{ textAlign: "center", mb: 4 }}>
          <img
            src="your-logo-placeholder.png"
            alt="Unhire logo placeholder"
            style={{ width: "110px", margin: "0 auto" }}
          />
          <Typography variant="srOnly">Sign up to Unhire</Typography>
        </Box>

        {/* Form */}
        <Box component="form" sx={{ display: "flex", flexDirection: "column", gap: 2 }}>
          <TextField
            type="email"
            placeholder="Enter email"
            fullWidth
            InputProps={{
              sx: {
                borderRadius: "50px",
                bgcolor: "white",
                "& input::placeholder": { color: "#d3c6e2" },
                "& fieldset": { borderColor: "#C49AF2" },
              },
            }}
          />

          <TextField
            type="text"
            placeholder="Enter full name"
            fullWidth
            InputProps={{
              sx: {
                borderRadius: "50px",
                bgcolor: "white",
                "& input::placeholder": { color: "#d3c6e2" },
                "& fieldset": { borderColor: "#C49AF2" },
              },
            }}
          />

          <TextField
            type={showPassword ? "text" : "password"}
            placeholder="Password"
            fullWidth
            InputProps={{
              sx: {
                borderRadius: "50px",
                bgcolor: "white",
                "& input::placeholder": { color: "#d3c6e2" },
                "& fieldset": { borderColor: "#C49AF2" },
              },
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton onClick={() => setShowPassword(!showPassword)} edge="end">
                    {showPassword ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              ),
            }}
          />

          <TextField
            type={showConfirmPassword ? "text" : "password"}
            placeholder="Confirm password"
            fullWidth
            InputProps={{
              sx: {
                borderRadius: "50px",
                bgcolor: "white",
                "& input::placeholder": { color: "#d3c6e2" },
                "& fieldset": { borderColor: "#C49AF2" },
              },
              endAdornment: (
                <InputAdornment position="end">
                  <IconButton
                    onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                    edge="end"
                  >
                    {showConfirmPassword ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              ),
            }}
          />

          <Button
            type="submit"
            fullWidth
            sx={{
              mt: 1,
              py: 1.2,
              borderRadius: "50px",
              bgcolor: "#C49AF2",
              color: "white",
              fontWeight: "600",
              textTransform: "none",
              "&:hover": { bgcolor: "#b27ae9" },
            }}
          >
            Sign up
          </Button>

          <Box sx={{ display: "flex", justifyContent: "center", mt: 2 }}>
            <Typography variant="body2">Already have an account?</Typography>
            <Typography
              variant="body2"
              component="a"
              href="#"
              sx={{ ml: 1, textDecoration: "underline", fontWeight: 500 }}
            >
              Login
            </Typography>
          </Box>
        </Box>
      </Card>
    </Box>
  );
}
