---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/add-vmstoragepath?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-VMStoragePath
---

# 添加虚拟机存储路径

## 摘要
为虚拟机配置存储路径。

## 语法

```
Add-VMStoragePath [-Path] <String[]> [-ResourcePoolName] <String[]> [-ResourcePoolType] <VMResourcePoolType>
 [-Passthru] [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

## 描述
`Add-VMStoragePath` cmdlet 可用于将路径添加到存储资源池中。

## 示例

### 示例 1
```
PS C:\> Add-VMStoragePath -Path D:\VHD -ResourcePoolName "Engineering Department" -ResourcePoolType VHD
```

将路径 D:\VHD 添加到资源存储池“Engineering Department”中，该存储池的类型为 VHD。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet的输出结果）。默认值是本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规选择 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个用于添加存储资源池路径的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址和完全限定的域名作为主机地址。默认值为本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规选择 value: None
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
默认值；常规选择 value: False
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
默认值；常规选择 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
表示此 cmdlet 返回一个 **字符串**（String）。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值；常规选择 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Path
指定要添加到存储资源池中的路径。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
默认值；常规选择 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ResourcePoolName
指定要添加路径的资源池的名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
默认值；常规选择 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ResourcePoolType
指定要为其添加存储路径的资源池的类型。允许的值有 **VFD**、**VHD** 和 **ISO**。

```yaml
Type: VMResourcePoolType
Parameter Sets: (All)
Aliases:
Accepted values: VHD, ISO, VFD

Required: True
Position: 2
默认值；常规选择 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet运行会发生的结果。但实际上，这个cmdlet并没有被运行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值；常规选择 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值；常规选择

### System.String
如果指定了 `-PassThru`。

## 备注

## 相关链接

