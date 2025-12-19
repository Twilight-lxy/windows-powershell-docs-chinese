---
description: 使用此主题可以通过 Windows PowerShell 来帮助管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/get-vmidecontroller?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-VMIdeController
---

# Get-VMIdeController

## 摘要
获取虚拟机或快照的IDE控制器信息。

## 语法

### VMName（默认值）
```
Get-VMIdeController [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-VMName] <String[]> [[-ControllerNumber] <Int32>] [<CommonParameters>]
```

### VMObject
```
Get-VMIdeController [-VM] <VirtualMachine[]> [[-ControllerNumber] <Int32>] [<CommonParameters>]
```

### VMSnapshot
```
Get-VMIdeController [-VMSnapshot] <VMSnapshot> [[-ControllerNumber] <Int32>] [<CommonParameters>]
```

## 描述
`Get-VMIdeController` cmdlet 可以获取虚拟机或快照的 IDE 控制器信息。

## 示例

### 示例 1
```
PS C:\> Get-VMIdeController TestVM
```

获取属于虚拟机 TestVM 的所有 IDE 控制器。

### 示例 2
```
PS C:\> Get-VMIdeController TestVM -ControllerNumber 0
```

获取属于虚拟机 TestVM 的第一个 IDE 控制器。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。您可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个 Hyper-V 主机，用于从中检索虚拟机或快照的 IDE 控制器。允许使用 NetBIOS 名称、IP 地址和完全限定域名作为主机标识。默认值为本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ControllerNumber
指定要检索的 IDE 控制器的编号。允许的值是 0 和 1。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: VMName
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VM
指定要检索其集成开发环境（IDE）控制器的虚拟机。

```yaml
Type: VirtualMachine[]
Parameter Sets: VMObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMName
指定要检索其 IDE 控制器的虚拟机的名称。

```yaml
Type: String[]
Parameter Sets: VMName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMSnapshot
指定要检索其IDE控制器的快照。

```yaml
Type: VMSnapshot
Parameter Sets: VMSnapshot
Aliases: VMCheckpoint

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMIdeController

## 备注

## 相关链接

