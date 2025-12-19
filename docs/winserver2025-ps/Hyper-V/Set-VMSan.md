---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/set-vmsan?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-VMSan
---

# Set-VMSan

## 摘要
在一个或多个Hyper-V主机上配置虚拟存储区域网络（SAN）。

## 语法

### HbaObject（默认值）
```
Set-VMSan [-Name] <String> [-HostBusAdapter <CimInstance[]>] [-Note <String>] [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### StringWwn
```
Set-VMSan [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String> -WorldWideNodeName <String[]> -WorldWidePortName <String[]> [-Note <String>] [-Passthru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
**Set-VMSan** cmdlet 可用于在一个或多个 Hyper-V 主机上配置虚拟存储区域网络（SAN）。

## 示例

### 示例 1
```
PS C:\> Set-VMSan -Name Production -WorldWideNodeName C003FF0000FFFF22 -WorldWidePortName C003FF5778E50024
```

使用指定的 `WorldWideNodeName` 和 `WorldWidePortName` 值来配置一个名为 “Production” 的虚拟存储区域网络（SAN）。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: StringWwn
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于配置虚拟存储区域网络（SAN）的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全 Qualified 域名进行标识。默认值为本地计算机；可以通过使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: StringWwn
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
默认值；常规设置 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: StringWwn
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HostBusAdapter
指定要与虚拟存储区域网络（SAN）关联的主机总线适配器（HBA）。您可以使用 **Get-InitiatorPort** cmdlet 来获取该对象。

```yaml
Type: CimInstance[]
Parameter Sets: HbaObject
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要配置的虚拟存储区域网络（SAN）的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: SanName

Required: True
Position: 0
默认值；常规设置 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Note
指定要与虚拟存储区域网络（SAN）关联的注释。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定某个对象将被传递到表示已配置的虚拟存储区域网络（SAN）的管道中。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值；常规设置 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorldWideNodeName
要与这个虚拟存储区域网络（SAN）关联的光纤通道主机总线适配器的全球通用名称（WWN）。

```yaml
Type: String[]
Parameter Sets: StringWwn
Aliases: Wwnn, NodeName, Wwnns, NodeNames, WorldWideNodeNames, NodeAddress

Required: True
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorldWidePortName
要与这个虚拟存储区域网络（SAN）关联的光纤通道主机总线适配器的全球通用端口名称。

```yaml
Type: String[]
Parameter Sets: StringWwn
Aliases: Wwpn, PortName, Wwpns, PortNames, WorldWidePortNames, PortAddress

Required: True
Position: Named
默认值；常规设置 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值；常规设置

### Microsoft.HyperV.PowerShell.SAN
如果指定了**-PassThru**选项。

## 备注

## 相关链接

