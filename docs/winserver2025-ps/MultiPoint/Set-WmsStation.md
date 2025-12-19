---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MultiPoint.dll-Help.xml
Module Name: MultiPoint
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/multipoint/set-wmsstation?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-WmsStation
---

# Set-WmsStation

## 摘要
修改站点信息。

## 语法

### FriendlyName
```
Set-WmsStation [-StationId] <UInt32[]> -FriendlyName <String> [-Server <String>] [<CommonParameters>]
```

### AutoLogonEnable
```
Set-WmsStation [-StationId] <UInt32[]> -AutoLogonCredential <PSCredential> [-OverrideAdminWarning]
 [-Server <String>] [<CommonParameters>]
```

### 禁用自动登录功能
```
Set-WmsStation [-StationId] <UInt32[]> [-DisableAutoLogon] [-Server <String>] [<CommonParameters>]
```

### RemoteConnection
```
Set-WmsStation [-StationId] <UInt32[]> -SessionHost <String> [-Server <String>] [<CommonParameters>]
```

### RemoteConnectionVM
```
Set-WmsStation [-StationId] <UInt32[]> -VmName <String> [-Server <String>] [<CommonParameters>]
```

### 禁用远程连接（DisableRemoteConnection）
```
Set-WmsStation [-StationId] <UInt32[]> [-LocalSessionHost] [-Server <String>] [<CommonParameters>]
```

### DisplayOrientation
```
Set-WmsStation [-StationId] <UInt32[]> -DisplayOrientation <EDisplayOrientationPS> [-Server <String>]
 [<CommonParameters>]
```

## 描述
`Set-WmsStation` cmdlet 用于修改站点信息。你可以使用这个 cmdlet 来设置站点的自动登录功能以及友好名称（即站点的显示名称）。如果你希望允许属于 Administrator 组的用户自动登录，请指定 `OverrideAdminWarning` 参数。

## 示例

### 示例 1：设置一个电台
```
PS C:\> $Creds = Get-Credential -UserName "Student01" -Message "Enter desired password"
PS C:\> Set-WmsStation -StationId 1 -FriendlyName -"Patti's Station" -AutoLogonCredential $Creds
```

第一个命令获取Student01的凭据信息，然后将这些信息存储在$Creds变量中。

第二个命令将站点1的友好名称设置为“Patti’s Station”。现在站点1已配置为使用用户名“Student01”自动登录。

## 参数

### -AutoLogonCredential
指定自动登录所需的凭据。可以使用 `Get-Credential` cmdlet 来获取一个 `PSCredential` 对象。

```yaml
Type: PSCredential
Parameter Sets: AutoLogonEnable
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableAutoLogon
禁用该站点的自动登录功能。

```yaml
Type: SwitchParameter
Parameter Sets: DisableAutoLogon
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisplayOrientation
指定车站的显示方向。

```yaml
Type: EDisplayOrientationPS
Parameter Sets: DisplayOrientation
Aliases:
Accepted values: Portrait, Landscape, PortraitFlipped, LandscapeFlipped

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FriendlyName
为该站点指定一个友好的名称。

```yaml
Type: String
Parameter Sets: FriendlyName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -LocalSessionHost
指定本地会话主机。

```yaml
Type: SwitchParameter
Parameter Sets: DisableRemoteConnection
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -OverrideAdminWarning
表示此操作会忽略管理员警告。请指定该参数以允许管理员自动登录。

```yaml
Type: SwitchParameter
Parameter Sets: AutoLogonEnable
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Server
指定作为该命令目标的多点服务器（MultiPoint Server）的完全限定主机名。默认值为 localhost。

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

### -SessionHost
指定会话主机。

```yaml
Type: String
Parameter Sets: RemoteConnection
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StationId
指定一个车站ID数组。

```yaml
Type: UInt32[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -VmName
用于指定虚拟桌面基础设施（VDI）工作站中的虚拟机客户端的主机名称。

```yaml
Type: String
Parameter Sets: RemoteConnectionVM
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.UInt32[]

### System.String

## 输出

### System.Object

## 备注

## 相关链接

[Clear-WmsStation](./Clear-WmsStation.md)

[Get-WmsStation](./Get-WmsStation.md)

[Join-WmsStation](./Join-WmsStation.md)

[Split-WmsStation](./Split-WmsStation.md)

[更新 WMS 站点](./Update-WmsStation.md)

