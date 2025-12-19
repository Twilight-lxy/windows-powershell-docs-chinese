---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmremotefxphysicalvideoadapter?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMRemoteFXPhysicalVideoAdapter
---

# 获取虚拟机（VM）的 RemoteFX 物理视频适配器

## 摘要
获取一台或多台Hyper-V主机上的RemoteFX物理图形适配器信息。

## 语法

### ComputerName（默认值）
```
Get-VMRemoteFXPhysicalVideoAdapter [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [[-Name] <String[]>] [<CommonParameters>]
```

### CimSession
```
Get-VMRemoteFXPhysicalVideoAdapter [-CimSession <CimSession[]>] [[-Name] <String[]>] [<CommonParameters>]
```

## 描述
`Get-VMRemoteFXPhysicalVideoAdapter` cmdlet 可以获取一个或多个 Hyper-V 主机上安装的 RemoteFX 物理图形适配器。

## 示例

### 示例 1
```
PS C:\> Get-VMRemoteFXPhysicalVideoAdapter
```

获取Hyper-V主机上的所有RemoteFX物理视频适配器。

### 示例 2
```
PS C:\> Get-VMRemoteFXPhysicalVideoAdapter -Name *Nvidia*
```

获取Hyper-V主机上所有的RemoteFX物理视频适配器，这些适配器的名称中包含“Nvidia”字样。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: CimSession
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个运行此 cmdlet 的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名来进行标识。默认值是本地计算机。可以使用 “localhost” 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: ComputerName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
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
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定一个或多个要检索的RemoteFX物理图形适配器的名称。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV POWERShell.VMRemoteFXPhysicalVideoAdapter

## 备注

## 相关链接

