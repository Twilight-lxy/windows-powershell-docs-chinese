---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmresourcepool?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMResourcePool
---

# 删除虚拟机资源池

## 摘要
从一个或多个虚拟机主机中删除资源池。

## 语法

### ComputerName（默认值）
```
Remove-VMResourcePool [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-Name] <String>
 [-ResourcePoolType] <VMResourcePoolType[]> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### CimSession
```
Remove-VMResourcePool [-CimSession <CimSession[]>] [-Name] <String> [-ResourcePoolType] <VMResourcePoolType[]>
 [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-VMResourcePool` cmdlet 用于从一个或多个虚拟机主机中删除资源池。

## 示例

### 示例 1
```
PS C:\> Remove-VMResourcePool Test VHD
```

删除一个名为“Test”的虚拟硬盘资源池。

## 参数

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。请输入计算机名称或会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: CimSession
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个运行此cmdlet的Hyper-V主机。可以使用NetBIOS名称、IP地址或完全qualified域名来进行指定。默认值为本地计算机。可以使用“localhost”或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: ComputerName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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
Parameter Sets: ComputerName
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定资源池的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 **VMResourcePool** 对象传递给流水线，该对象代表被移除的资源池。

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
指定要删除的资源池的类型。

```yaml
Type: VMResourcePoolType[]
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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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
如果指定了**-PassThru**选项。

## 备注

## 相关链接

