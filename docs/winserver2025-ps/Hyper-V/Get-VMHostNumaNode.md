---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmhostnumanode?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMHostNumaNode
---

# Get-VMHostNumaNode

## 摘要
获取虚拟机主机的NUMA（Non-Uniform Memory Access）节点信息。

## 语法

### ComputerName（默认值）
```
Get-VMHostNumaNode [[-ComputerName] <String[]>] [[-Credential] <PSCredential[]>] [-Id <Int32>]
 [<CommonParameters>]
```

### CimSession
```
Get-VMHostNumaNode [-CimSession] <CimSession[]> [-Id <Int32>] [<CommonParameters>]
```

## 描述
`Get-VMHostNumaNode` cmdlet 可以获取 Hyper-V 主机的 NUMA（非均匀内存分配）拓扑结构，并为主机上的每个 NUMA 节点返回一个 `VMHostNumaNode` 对象。

## 示例

### 示例 1
```
PS C:\> Get-VMHostNumaNode
```

获取本地 Hyper-V 主机的 NUMA（非统一内存架构）拓扑信息。

## 参数

### -CimSession
在远程会话或远程计算机上运行该 cmdlet。可以输入计算机名称，或者输入一个会话对象（例如 [New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认情况下，该 cmdlet 会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: CimSession
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个运行此 cmdlet 的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址和完全限定域名作为主机标识。默认值为本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: ComputerName
Aliases:

Required: False
Position: 0
Default value: None
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
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Id
用于识别一个NUMA节点，以便从中获取**VMHostNumaNode**信息。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMHostNumaNode

## 备注

## 相关链接

