// components/common/Layout.jsx
import React, { useState, useEffect } from 'react'
import { Outlet, Link, useLocation, useNavigate } from 'react-router-dom'
import { 
  AppBar, 
  Toolbar, 
  Typography, 
  Button, 
  IconButton, 
  Drawer, 
  List, 
  ListItem, 
  ListItemText,
  ListItemIcon,
  Box,
  useMediaQuery,
  useTheme,
  Badge,
  Menu,
  MenuItem,
  Avatar,
  Container,
  Divider,
  Grid
} from '@mui/material'
import {
  Menu as MenuIcon,
  ShoppingCart,
  Person,
  ExitToApp,
  Dashboard,
  Home,
  Store,
  ShoppingBag,
  LocalShipping,
  AdminPanelSettings,
  Chat as ChatIcon,
  Email,
  Phone
} from '@mui/icons-material'
import { useAuth } from '../../contexts/AuthContext'
import './Layout.css'
import logo1 from '../../assets/logo.png';

const Layout = () => {
  const { user, logout, isAuthenticated } = useAuth()
  const location = useLocation()
  const navigate = useNavigate()
  const theme = useTheme()
  const isMobile = useMediaQuery(theme.breakpoints.down('md'))
  const isSmallMobile = useMediaQuery(theme.breakpoints.down('sm'))
  const [drawerOpen, setDrawerOpen] = useState(false)
  const [scrolled, setScrolled] = useState(false)
  const [anchorEl, setAnchorEl] = useState(null)
  const [cartItemsCount, setCartItemsCount] = useState(0)

  // Nouvelle palette de couleurs
  const colorPalette = {
    primary: '#2C3E50',    // Bleu foncé
    secondary: '#E74C3C',  // Rouge vif
    accent: '#27AE60',     // Vert émeraude
    background: '#F9F9F9', // Fond très clair
    surface: '#FFFFFF',    // Surface blanche
    textPrimary: '#2C3E50', // Texte principal foncé
    textSecondary: '#7F8C8D', // Texte secondaire gris
    navBackground: 'rgba(255, 255, 255, 0.98)', // Fond navigation blanc
    footerBackground: '#34495E', // Fond footer bleu nuit
    footerText: '#ECF0F1'  // Texte footer clair
  }

  // Gestion du défilement
  useEffect(() => {
    const handleScroll = () => {
      const isScrolled = window.scrollY > 50
      setScrolled(isScrolled)
    }

    window.addEventListener('scroll', handleScroll, { passive: true })
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const handleLogout = () => {
    logout()
    setDrawerOpen(false)
    setAnchorEl(null)
    navigate('/')
  }

  const handleProfileMenuOpen = (event) => {
    setAnchorEl(event.currentTarget)
  }

  const handleProfileMenuClose = () => {
    setAnchorEl(null)
  }

  const handleDashboard = () => {
    const userRole = user?.role || user?.user_type
    if (userRole === 'admin') {
      navigate('/admin')
    } else if (userRole === 'farmer') {
      navigate('/farmer')
    } else if (userRole === 'delivery') {
      navigate('/delivery')
    } else {
      navigate('/customer')
    }
    setDrawerOpen(false)
    handleProfileMenuClose()
  }

  const getDashboardIcon = () => {
    const userRole = user?.role || user?.user_type
    switch (userRole) {
      case 'admin': return <AdminPanelSettings />
      case 'farmer': return <Store />
      case 'delivery': return <LocalShipping />
      default: return <Dashboard />
    }
  }

  const getDashboardLabel = () => {
    const userRole = user?.role || user?.user_type
    switch (userRole) {
      case 'admin': return 'Administration'
      case 'farmer': return 'Tableau Agriculteur'
      case 'delivery': return 'Livraisons'
      default: return 'Mon Compte'
    }
  }

  const navigationItems = [
    { path: '/', label: 'Accueil', icon: <Home /> },
    { path: '/products', label: 'Produits', icon: <Store /> },
  ]

  if (isAuthenticated) {
    const userRole = user?.role || user?.user_type
    
    if (userRole === 'farmer') {
      navigationItems.push(
        { path: '/farmer', label: 'Tableau de bord', icon: <Dashboard /> },
        { path: '/orders', label: 'Commandes', icon: <ShoppingBag /> },
        { path: '/chat', label: 'Messages', icon: <ChatIcon /> }
      )
    } else if (userRole === 'customer' || userRole === 'buyer') {
      navigationItems.push(
        { path: '/customer', label: 'Mon compte', icon: <Dashboard /> },
        { path: '/cart', label: 'Panier', icon: <ShoppingCart /> },
        { path: '/orders', label: 'Mes commandes', icon: <ShoppingBag /> },
        { path: '/chat', label: 'Messages', icon: <ChatIcon /> }
      )
    } else if (userRole === 'admin') {
      navigationItems.push(
        { path: '/admin', label: 'Administration', icon: <AdminPanelSettings /> }
      )
    } else if (userRole === 'delivery') {
      navigationItems.push(
        { path: '/delivery', label: 'Livraisons', icon: <LocalShipping /> }
      )
    }
  }

  const renderNavigation = () => (
    <List sx={{ py: 0 }}>
      {navigationItems.map((item, index) => (
        <ListItem 
          key={item.path} 
          component={Link} 
          to={item.path}
          onClick={() => setDrawerOpen(false)}
          className={`${location.pathname === item.path ? 'active-nav-item' : ''} fade-in-left`}
          style={{ 
            animationDelay: `${index * 0.1}s`,
            borderBottom: '1px solid rgba(44, 62, 80, 0.1)',
            color: colorPalette.textPrimary
          }}
          sx={{
            '&:hover': {
              backgroundColor: 'rgba(39, 174, 96, 0.08)',
              color: colorPalette.accent
            }
          }}
        >
          <ListItemIcon sx={{ minWidth: 40, color: colorPalette.textPrimary }}>
            {React.cloneElement(item.icon, { style: { color: colorPalette.textPrimary } })}
          </ListItemIcon>
          <ListItemText 
            primary={item.label} 
            primaryTypographyProps={{ 
              fontSize: '0.95rem',
              color: 'inherit'
            }}
          />
        </ListItem>
      ))}
      {isAuthenticated && (
        <>
          <Divider sx={{ my: 1, borderColor: 'rgba(44, 62, 80, 0.1)' }} />
          <ListItem 
            button
            onClick={handleLogout}
            className="logout-button fade-in-left"
            style={{ animationDelay: `${navigationItems.length * 0.1}s` }}
            sx={{
              '&:hover': {
                backgroundColor: 'rgba(231, 76, 60, 0.1)',
                color: colorPalette.secondary
              }
            }}
          >
            <ListItemIcon sx={{ minWidth: 40, color: colorPalette.secondary }}>
              <ExitToApp />
            </ListItemIcon>
            <ListItemText 
              primary="Déconnexion" 
              primaryTypographyProps={{ color: colorPalette.secondary }}
            />
          </ListItem>
        </>
      )}
    </List>
  )

  return (
    <div className="layout" style={{ backgroundColor: colorPalette.background }}>
      <AppBar 
        position="fixed" 
        className={`app-bar ${scrolled ? 'scrolled' : ''}`}
        sx={{
          backgroundColor: colorPalette.navBackground,
          backdropFilter: scrolled ? 'blur(10px)' : 'none',
          transition: 'all 0.3s ease',
          boxShadow: scrolled ? '0 4px 20px rgba(0,0,0,0.08)' : '0 1px 3px rgba(0,0,0,0.1)',
          color: colorPalette.textPrimary
        }}
      >
        <Container maxWidth="xl">
          <Toolbar sx={{ py: 1, minHeight: { xs: 70, md: 80 } }}>
            {/* Logo */}
            <Box 
              className="logo-section"
              sx={{ 
                display: 'flex', 
                alignItems: 'center',
                flexShrink: 0
              }}
            >
              <img 
                src={logo1} 
                alt="TERRABIA" 
                style={{ 
                  height: '160px', 
                  marginBottom: '21px',
                  borderRadius: '8px',
                  cursor: 'pointer',
                  filter: 'brightness(1.1) contrast(1.1)'
                }} 
                className="logo"
                onClick={() => navigate('/')}
              />
            </Box>

            {/* Navigation pour desktop */}
            {!isMobile && (
              <Box 
                className="nav-section"
                sx={{ 
                  display: 'flex', 
                  flex: 1, 
                  justifyContent: 'center',
                  mx: 4
                }}
              >
                {navigationItems.map((item, index) => (
                  <Button
                    key={item.path}
                    component={Link}
                    to={item.path}
                    startIcon={!isSmallMobile && item.icon}
                    className={`${location.pathname === item.path ? 'active-nav-button' : ''} fade-in-down`}
                    style={{ animationDelay: `${index * 0.1}s` }}
                    sx={{
                      mx: 1,
                      px: 2,
                      borderRadius: 2,
                      fontWeight: location.pathname === item.path ? 600 : 400,
                      backgroundColor: location.pathname === item.path ? 'rgba(39, 174, 96, 0.12)' : 'transparent',
                      color: location.pathname === item.path ? colorPalette.accent : colorPalette.textPrimary,
                      '&:hover': {
                        backgroundColor: 'rgba(39, 174, 96, 0.08)',
                        color: colorPalette.accent
                      },
                      '& .MuiButton-startIcon': {
                        color: location.pathname === item.path ? colorPalette.accent : colorPalette.textSecondary
                      }
                    }}
                  >
                    {isSmallMobile ? React.cloneElement(item.icon, { fontSize: 'small' }) : item.label}
                  </Button>
                ))}
              </Box>
            )}

            {/* Section authentification */}
            <Box 
              className="auth-section"
              sx={{ 
                display: 'flex', 
                alignItems: 'center',
                flexShrink: 0
              }}
            >
              {isAuthenticated ? (
                <Box className="user-info fade-in-right" sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  {(user?.role === 'customer' || user?.role === 'buyer' || user?.user_type === 'customer' || user?.user_type === 'buyer') && (
                    <IconButton 
                      component={Link} 
                      to="/cart"
                      size="medium"
                      className="cart-badge"
                      sx={{ 
                        position: 'relative',
                        color: colorPalette.textPrimary,
                        '&:hover': { 
                          backgroundColor: 'rgba(39, 174, 96, 0.08)',
                          color: colorPalette.accent
                        }
                      }}
                    >
                      <Badge badgeContent={cartItemsCount} color="error">
                        <ShoppingCart />
                      </Badge>
                    </IconButton>
                  )}
                  
                  <IconButton
                    onClick={handleProfileMenuOpen}
                    size="medium"
                    sx={{ 
                      ml: 1,
                      color: colorPalette.textPrimary,
                      '&:hover': { 
                        backgroundColor: 'rgba(39, 174, 96, 0.08)',
                        color: colorPalette.accent
                      }
                    }}
                  >
                    <Avatar 
                      className="user-avatar"
                      sx={{ 
                        width: 36, 
                        height: 36, 
                        bgcolor: colorPalette.accent,
                        color: '#FFFFFF',
                        fontSize: '0.9rem',
                        fontWeight: 600
                      }}
                    >
                      {user?.first_name?.[0]?.toUpperCase() || user?.name?.[0]?.toUpperCase() || <Person />}
                    </Avatar>
                  </IconButton>
                  
                  {!isMobile && (
                    <Typography variant="body2" className="user-name" sx={{ color: colorPalette.textPrimary }}>
                      {user?.first_name || user?.name || 'Utilisateur'}
                    </Typography>
                  )}
                  
                  <Menu
                    anchorEl={anchorEl}
                    open={Boolean(anchorEl)}
                    onClose={handleProfileMenuClose}
                    PaperProps={{
                      elevation: 8,
                      sx: {
                        mt: 1.5,
                        minWidth: 200,
                        backgroundColor: colorPalette.surface,
                        color: colorPalette.textPrimary,
                        '& .MuiMenuItem-root': {
                          px: 2,
                          py: 1.5,
                          '&:hover': {
                            backgroundColor: 'rgba(39, 174, 96, 0.08)',
                            color: colorPalette.accent
                          }
                        }
                      }
                    }}
                    transformOrigin={{ horizontal: 'right', vertical: 'top' }}
                    anchorOrigin={{ horizontal: 'right', vertical: 'bottom' }}
                  >
                    <MenuItem onClick={handleDashboard}>
                      <ListItemIcon sx={{ color: colorPalette.textPrimary }}>
                        {getDashboardIcon()}
                      </ListItemIcon>
                      <ListItemText 
                        primary={getDashboardLabel()} 
                        primaryTypographyProps={{ 
                          variant: 'body2', 
                          fontWeight: 500,
                          color: colorPalette.textPrimary 
                        }}
                      />
                    </MenuItem>
                    <Divider sx={{ borderColor: 'rgba(44, 62, 80, 0.1)' }} />
                    <MenuItem onClick={handleLogout}>
                      <ListItemIcon sx={{ color: colorPalette.secondary }}>
                        <ExitToApp fontSize="small" />
                      </ListItemIcon>
                      <ListItemText 
                        primary="Déconnexion" 
                        primaryTypographyProps={{ 
                          color: colorPalette.secondary, 
                          variant: 'body2' 
                        }}
                      />
                    </MenuItem>
                  </Menu>
                </Box>
              ) : (
                <Box className="fade-in-right" sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <Button 
                    component={Link} 
                    to="/login"
                    startIcon={!isSmallMobile && <Person />}
                    sx={{
                      borderRadius: 2,
                      color: colorPalette.textPrimary,
                      '&:hover': { 
                        backgroundColor: 'rgba(39, 174, 96, 0.08)',
                        color: colorPalette.accent
                      }
                    }}
                  >
                    {isSmallMobile ? <Person /> : 'Connexion'}
                  </Button>
                  {!isSmallMobile && (
                    <Button 
                      variant="contained" 
                      sx={{ 
                        backgroundColor: colorPalette.accent,
                        color: '#FFFFFF',
                        borderRadius: 2,
                        '&:hover': {
                          backgroundColor: '#219653',
                          boxShadow: '0 4px 12px rgba(39, 174, 96, 0.3)'
                        }
                      }}
                      component={Link} 
                      to="/register"
                    >
                      Inscription
                    </Button>
                  )}
                </Box>
              )}

              {isMobile && (
                <IconButton
                  edge="end"
                  aria-label="menu"
                  onClick={() => setDrawerOpen(true)}
                  className="fade-in-right"
                  sx={{ 
                    ml: 1,
                    color: colorPalette.textPrimary,
                    '&:hover': { 
                      backgroundColor: 'rgba(39, 174, 96, 0.08)',
                      color: colorPalette.accent
                    }
                  }}
                >
                  <MenuIcon />
                </IconButton>
              )}
            </Box>
          </Toolbar>
        </Container>
      </AppBar>

      {/* Drawer mobile */}
      <Drawer
        anchor="right"
        open={drawerOpen}
        onClose={() => setDrawerOpen(false)}
        PaperProps={{
          sx: {
            width: 280,
            maxWidth: '80vw',
            backgroundColor: colorPalette.surface,
            color: colorPalette.textPrimary
          }
        }}
      >
        <Box className="drawer-header" sx={{ backgroundColor: colorPalette.primary, color: '#FFFFFF' }}>
          <Typography variant="h6" component="div" sx={{ p: 2 }}>
            TERRABIA
          </Typography>
        </Box>
        <Box className="drawer-list">
          {renderNavigation()}
        </Box>
      </Drawer>

      {/* Espace pour la barre d'appbar fixe */}
      <Toolbar sx={{ minHeight: { xs: 70, md: 80 } }} />

      <main className={`main-content ${scrolled ? 'scrolled' : ''}`} style={{ backgroundColor: colorPalette.background }}>
        <Outlet />
      </main>

      {/* Footer */}
      <footer className="footer" style={{ backgroundColor: colorPalette.footerBackground, color: colorPalette.footerText }}>
        <Container maxWidth="xl">
          <Box className="footer-content">
            <Grid container spacing={4}>
              <Grid item xs={12} md={4}>
                <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: { xs: 'center', md: 'flex-start' } }} className="fade-in-up">
                  <img 
                    src={logo1} 
                    alt="TERRABIA" 
                    style={{ 
                      height: '160px', 
                      marginBottom: '16px',
                      borderRadius: '8px',
                      filter: 'brightness(1.2)'
                    }} 
                  />
                  <Typography variant="body2" className="footer-description" sx={{ color: colorPalette.footerText }}>
                    Votre marché agricole en ligne - Produits frais du Cameroun et du monde
                  </Typography>
                </Box>
              </Grid>

              <Grid item xs={12} sm={6} md={4}>
                <Box sx={{ textAlign: { xs: 'center', sm: 'left' } }} className="fade-in-up" style={{ animationDelay: '0.1s' }}>
                  <Typography variant="h6" gutterBottom sx={{ fontWeight: 600, color: colorPalette.footerText }}>
                    Liens Rapides
                  </Typography>
                  <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
                    <Button color="inherit" component={Link} to="/about" sx={{ 
                      justifyContent: { xs: 'center', sm: 'flex-start' },
                      color: colorPalette.footerText,
                      '&:hover': { color: '#FFFFFF' }
                    }}>
                      À propos
                    </Button>
                    <Button color="inherit" component={Link} to="/contact" sx={{ 
                      justifyContent: { xs: 'center', sm: 'flex-start' },
                      color: colorPalette.footerText,
                      '&:hover': { color: '#FFFFFF' }
                    }}>
                      Contact
                    </Button>
                    <Button color="inherit" component={Link} to="/terms" sx={{ 
                      justifyContent: { xs: 'center', sm: 'flex-start' },
                      color: colorPalette.footerText,
                      '&:hover': { color: '#FFFFFF' }
                    }}>
                      Conditions d'utilisation
                    </Button>
                  </Box>
                </Box>
              </Grid>

              <Grid item xs={12} sm={6} md={4}>
                <Box sx={{ textAlign: { xs: 'center', sm: 'left' } }} className="fade-in-up" style={{ animationDelay: '0.2s' }}>
                  <Typography variant="h6" gutterBottom sx={{ fontWeight: 600, color: colorPalette.footerText }}>
                    Contact
                  </Typography>
                  <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1, alignItems: { xs: 'center', sm: 'flex-start' } }}>
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, color: colorPalette.footerText }}>
                      <Email fontSize="small" />
                      <Typography variant="body2">contact@terrabia.com</Typography>
                    </Box>
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, color: colorPalette.footerText }}>
                      <Phone fontSize="small" />
                      <Typography variant="body2">+237 XXX XXX XXX</Typography>
                    </Box>
                  </Box>
                </Box>
              </Grid>
            </Grid>

            <Box sx={{ textAlign: 'center', mt: 4, pt: 2, borderTop: '1px solid rgba(255,255,255,0.2)' }}>
              <Typography variant="body2" className="copyright" sx={{ color: colorPalette.footerText }}>
                © 2024 TERRABIA. Tous droits réservés.
              </Typography>
            </Box>
          </Box>
        </Container>
      </footer>
    </div>
  )
}

export default Layout