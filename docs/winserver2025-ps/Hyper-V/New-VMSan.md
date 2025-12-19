---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/new-vmsan?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-VMSan
---

# 新VMSsan

## 摘要
在Hyper-V主机上创建一个新的虚拟存储区域网络（SAN）。

## 语法

### HbaObject（默认值）
```
New-VMSan [-CimSession <CimSession>] [-ComputerName <String>] [-Credential <PSCredential>] [-Name] <String>
 [-Note <String>] [-HostBusAdapter <CimInstance[]>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### StringWwn
```
New-VMSan [-CimSession <CimSession>] [-ComputerName <String>] [-Credential <PSCredential>] [-Name] <String>
 [-Note <String>] -WorldWideNodeName <String[]> -WorldWidePortName <String[]> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`New-VMSan` cmdlet 可在 Hyper-V 主机上创建一个新的虚拟存储区域网络（SAN）。

## 示例

### 示例 1
```
PS C:\> New-VMSan -Name Production -Note "Production SAN" -WorldWideNodeName C003FF0000FFFF00 -WorldWidePortName C003FF5778E50002
```

创建一个新的虚拟存储区域网络（SAN），并指定其名称（Name）、备注（Note）、全球节点名称（WorldWideNodeName）以及全球端口号名称（WorldWidePortName）。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定用于创建新的虚拟存储区域网络（SAN）的 Hyper-V 主机的友好名称。可以使用 NetBIOS 名称、IP 地址或完全限定域名。默认值为本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您确认是否要继续执行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HostBusAdapter
指定要与要创建的虚拟存储区域网络（SAN）关联的主机总线适配器（HBA）。可以通过运行 **Get-InitiatorPort** cmdlet 来获取相关信息。

```yaml
Type: CimInstance[]
Parameter Sets: HbaObject
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要创建的虚拟存储区域网络（SAN）的友好名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: SanName

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Note
指定一条备注信息，以便将其关联到即将创建的虚拟存储区域网络（SAN）上。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
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
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorldWideNodeName
指定要与要创建的虚拟存储区域网络（SAN）关联的主机总线适配器的全球唯一节点名称（WWNN）。

```yaml
Type: String[]
Parameter Sets: StringWwn
Aliases: Wwnn, NodeName, Wwnns, NodeNames, WorldWideNodeNames, NodeAddress

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorldWidePortName
指定要与即将创建的虚拟存储区域网络（SAN）关联的主机总线适配器的全球端口名称（WWPN）。

```yaml
Type: String[]
Parameter Sets: StringWwn
Aliases: Wwpn, PortName, Wwpns, PortNames, WorldWidePortNames, PortAddress

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV POWERShel.VMSan

## 备注

## 相关链接

