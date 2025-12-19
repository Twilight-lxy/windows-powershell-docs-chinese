---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/connect-vmsan?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Connect-VMSan
---

# Connect-VMSan

## 摘要
将主机总线适配器关联到虚拟存储区域网络（SAN）。

## 语法

### StringWwn（默认值）
```
Connect-VMSan [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String> -WorldWideNodeName <String[]> -WorldWidePortName <String[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### HbaObject
```
Connect-VMSan [-Name] <String> -HostBusAdapter <CimInstance[]> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Connect-VMSan` cmdlet 将主机总线适配器与虚拟存储区域网络（SAN）关联起来。

## 示例

### 示例 1
```
PS C:\> Connect-VMSan -Name Production -WorldWideNodeName C003FF0000FFFF00 -WorldWidePortName C003FF5778E50002
```

将名为“Production”的虚拟存储区域网络（SAN）与具有指定全球节点名称和全球端点名称的主机总线适配器关联起来。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。输入一个计算机名称或会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: StringWwn
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个 Hyper-V 主机，以便将主机总线适配器与虚拟存储区域网络（SAN）关联起来。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行指定。默认值为本地计算机。可以使用 `localhost` 或点号（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: StringWwn
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: True (ByPropertyName)
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
默认值 value: False
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
默认值 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -HostBusAdapter
指定要与虚拟存储区域网络（SAN）关联的主机总线适配器。

```yaml
Type: CimInstance[]
Parameter Sets: HbaObject
Aliases:

Required: True
Position: Named
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name
指定要与主机总线适配器关联的虚拟存储区域网络（SAN）的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases: SanName

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 **Microsoft.HyperV.Powershell.VMSan** 对象传递给管道，该对象代表要与主机总线适配器关联的虚拟存储区域网络（SAN）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorldWideNodeName
指定要与虚拟存储区域网络（SAN）关联的主机总线适配器的全球唯一节点名称。

```yaml
Type: String[]
Parameter Sets: StringWwn
Aliases: Wwnn, NodeName, Wwnns, NodeNames, WorldWideNodeNames, NodeAddress

Required: True
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WorldWidePortName
该主机总线适配器的全球通用名称，用于将其与虚拟存储区域网络（SAN）关联起来。

```yaml
Type: String[]
Parameter Sets: StringWwn
Aliases: Wwpn, PortName, Wwpns, PortNames, WorldWidePortNames, PortAddress

Required: True
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### Microsoft.HyperV.Powershell.VMSan
如果指定了 `-PassThru`，则……

## 备注

## 相关链接

