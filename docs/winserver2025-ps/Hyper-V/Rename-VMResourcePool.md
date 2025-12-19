---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/rename-vmresourcepool?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Rename-VMResourcePool
---

# 重命名虚拟机资源池

## 摘要
在一个或多个Hyper-V主机上重命名资源池。

## 语法

```
Rename-VMResourcePool [-CimSession <CimSession[]>] [-Name] <String> [-ResourcePoolType] <VMResourcePoolType>
 [-NewName] <String> [-Passthru] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Rename-VMResourcePool` 这个 cmdlet 可以更改一个或多个 Hyper-V 主机上资源池的名称。

## 示例

### 示例 1
```
PS C:\> Rename-VMResourcePool Test VHD Production
```

将一个VHD资源池的名称从“Test”更改为“Production”。

## 参数

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入一个计算机名称，或者提供一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于重命名资源池的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全合格的域名进行识别。默认值为本地计算机；可以使用 `localhost` 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前，会提示您进行确认。

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
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定要重命名的资源池的友好名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -NewName
指定要将指定的资源池重命名的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 2
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 **VMResourcePool** 对象传递给流水线，该对象代表需要重命名的资源池。

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

### -ResourcePoolType
指定需要重命名的资源池的类型。

```yaml
Type: VMResourcePoolType
Parameter Sets: (All)
Aliases:
Accepted values: Memory, Processor, Ethernet, VHD, ISO, VFD, FibreChannelPort, FibreChannelConnection, PciExpress

Required: True
Position: 1
默认值 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### VMResourcePool
如果指定了 `-PassThru`，则……

## 备注

## 相关链接

