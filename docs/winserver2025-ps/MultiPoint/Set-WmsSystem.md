---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/set-wmssystem?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WmsSystem
---

# Set-WmsSystem

## 摘要
修改系统属性。

## 语法

```
Set-WmsSystem [-BootToConsoleMode <Boolean>] [-DesktopMonitoring <Boolean>] [-IM <Boolean>]
 [-IPPerSession <Boolean>] [-Mode <SystemOperatingModePS>] [-SingleSessionPerUser <Boolean>]
 [-SuppressPrivacyNotification <Boolean>] [-AdminOrchestration <Boolean>] [-Server <String>]
 [<CommonParameters>]
```

## 描述
`Set-WmsSystem` cmdlet 用于修改多点服务器（MultiPoint Server）系统的系统属性。

## 示例

#### 示例 1：修改系统设置
```
PS C:\> Set-WmsSystem -CEIP $True -DesktopMonitoring $True
```

此命令为当前系统启用了客户体验改善计划（CEIP），同时还能对当前系统的桌面环境进行监控。

## 参数

### -AdminOrchestration
指示是否允许管理员进行编排（Orchestration）。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: IsAdminOrchestrationEnabled

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -BootToConsoleMode
指示是否启用“从启动状态切换到控制台模式”的功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -DesktopMonitoring
表示是否允许进行桌面监控。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: IsDesktopMonitoringAllowed

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IM
表示是否启用聊天功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: IsChatEnabled

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -IPPerSession
表示是否为每个会话分配一个唯一的IP地址。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: IsIPPerSessionEnabled

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Mode
指定模式。该参数的可接受值为：Console（控制台）和MultiStation（多站点）。

```yaml
Type: SystemOperatingModePS
Parameter Sets: (All)
Aliases:
Accepted values: Console, MultiStation

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定该命令的目标多点服务器（MultiPoint Server）的完整主机名。默认值为“localhost”。

```yaml
Type: String
Parameter Sets: (All)
Aliases: ComputerName

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SingleSessionPerUser
表示用户是否可以使用相同的用户名登录多个工作站。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases: IsSingleSessionPerUser

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -SuppressPrivacyNotification
表示是否禁用标准用户的隐私通知功能。

```yaml
Type: Boolean
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### `SystemNullable`  
1[[`System(Boolean`, `mscorlib`, `Version=4.0.0.0`, `Culture=neutral`, `PublicKeyToken=b77a5c561934e089`]]

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Add-WmsSystem](./Add-WmsSystem.md)

[Get-WmsSystem](./Get-WmsSystem.md)

[Remove-WmsSystem](./Remove-WmsSystem.md)

[重启 WMS 系统](./Restart-WmsSystem.md)

[Search-WmsSystem](./Search-WmsSystem.md)

[Stop-WmsSystem](./Stop-WmsSystem.md)

